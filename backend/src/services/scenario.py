from fastapi import HTTPException, status
from sqlmodel import col, desc, select, func
from src.models.dto.scenario import ScenarioModel
from src.models.project import Scenario
from src.services.base import BaseService


class ScenarioService(BaseService):
    async def get(self, scenario_id: str, current_version: str) -> Scenario:
        statement = (
            select(Scenario)
            .where(Scenario.scenario_id == scenario_id)
            .where(Scenario.current_version == current_version)
        )
        scenario = (await self.session.exec(statement)).one_or_none()
        if not scenario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"scenario not found. scenario_id={scenario_id} current_version={current_version}"
            )
        return scenario

    async def get_all(
        self,
        project_id: str,
        current_version: str,
        name: str,
        current_scenario: int = 0,
        scenario_size: int = 10,
    ):
        statement = (
            select(Scenario)
            .where(Scenario.project_id == project_id)
            .where(Scenario.current_version == current_version)
        )
        if name:
            statement = statement.where(col(Scenario.name).like(f"%{name}%"))
        statement = statement.offset(current_scenario * scenario_size)
        statement = statement.limit(scenario_size)
        statement.order_by(desc(Scenario.created_at))

        total = (
            await self.session.exec(select(func.count()).select_from(Scenario))
        ).one()
        scenarios = (await self.session.exec(statement)).all()

        return {"total": total, "scenarios": scenarios}

    async def create(
        self,
        tenant_id: str,
        project_id: str,
        current_version: str,
        scenario_model: ScenarioModel,
    ):

        scenario = Scenario(
            name=scenario_model.name,
            project_id=project_id,
            tenant_id=tenant_id,
            current_version=current_version,
        )
        self.session.add(scenario)
        await self.session.flush()
        await self.session.commit()

    async def update(
        self, scenario_id: str, current_version: str, scenario_model: ScenarioModel
    ):
        scenario = await self.get(
            scenario_id=scenario_id, current_version=current_version
        )
        scenario_dict = scenario_model.model_dump()
        for name, value in scenario_dict.items():
            setattr(scenario, name, value)

        self.session.add(scenario)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(scenario)

    async def remove(self, scenario_id: str, current_version: str):
        scenario = await self.get(scenario_id, current_version)
        await self.session.delete(scenario)
        await self.session.flush()
        await self.session.commit()
