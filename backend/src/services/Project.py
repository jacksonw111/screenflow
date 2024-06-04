from fastapi import HTTPException, status
from sqlmodel import desc, select, func

from src.models.dto.project import ProjectModel
from src.models.project import Project, ProjectStatus, ProjectVersion
from src.services.base import BaseService


class ProjectService(BaseService):
    async def create(self, project: ProjectModel, tenant_id: str):
        async with self.session.begin():
            project_obj = Project(
                name=project.name,
                description=project.description,
                tenant_id=tenant_id,
            )
            self.session.add(project_obj)
            await self.session.flush()
            self.session.add(
                ProjectVersion(
                    tenant_id=tenant_id,
                    project_id=project_obj.id,
                    name=project.current_version_name,
                    description=project.current_version_description,
                    is_current_version=True,
                )
            )
            await self.session.flush()
            await self.session.commit()

    async def get_by_id(self, project_id: str):
        statement = select(Project).where(Project.id == project_id)
        project = (await self.session.exec(statement)).one_or_none()

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"project not found. id={project_id}",
            )
        return project

    async def get_all(
        self,
        tenant_id: str,
        name: str = None,
        current_page: int = 0,
        page_size: int = 10,
    ):
        statement = select(Project).where(Project.tenant_id == tenant_id)
        if name:
            statement = statement.where(Project.name == name).where(
                Project.status == ProjectStatus.ACTIVE
            )

        statement = statement.offset(current_page * page_size)
        statement = statement.limit(page_size)
        statement = statement.order_by(desc(Project.created_at))

        total = (
            await self.session.exec(select(func.count()).select_from(Project))
        ).one()
        projects = (await self.session.exec(statement)).all()
        return {"total": total, "projects": projects}

    async def remove(self, project_id):
        project: Project = await self.get_by_id(project_id)
        project.status = ProjectStatus.DELETED
        self.session.add(project)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(project)

    async def update(self, project_id: str, project: ProjectModel):
        project_db = await self.get_by_id(project_id)
        project_dict = project.model_dump()
        for key, value in project_dict.items():
            setattr(project_db, key, value)
        self.session.add(project_db)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(project_db)
