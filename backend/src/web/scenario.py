from typing import Annotated
from fastapi import APIRouter, Depends, Request

from src.models.dto.scenario import ScenarioModel
from src.services.scenario import ScenarioService


api = APIRouter(prefix="/scenarios")


@api.get("")
async def get_all(
    service: Annotated[ScenarioService, Depends()],
    request: Request,
    name: str = None,
    current_scenario: int = 0,
    scenario_size: int = 10,
):
    return await service.get_all(
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
        name=name,
        current_scenario=current_scenario,
        scenario_size=scenario_size,
    )


@api.post("")
async def create(
    service: Annotated[ScenarioService, Depends()], scenario: ScenarioModel, request: Request
):
    await service.create(
        scenario_model=scenario,
        tenant_id=request.state.tenant_id,
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
    )


@api.put("/{scenario_id}")
async def update(
    service: Annotated[ScenarioService, Depends()],
    scenario_id: str,
    scenario: ScenarioModel,
    request: Request,
):
    await service.update(
        scenario_id=scenario_id,
        current_version=request.state.current_version_id,
        scenario_model=scenario,
    )


@api.delete("/{scenario_id}")
async def remove(
    service: Annotated[ScenarioService, Depends()],
    scenario_id: str,
    request: Request,
):
    await service.remove(
        scenario_id=scenario_id, current_version=request.state.current_version_id
    )
