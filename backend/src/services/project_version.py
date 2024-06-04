from fastapi import HTTPException, status
from sqlmodel import select
from src.models.project import ProjectVersion
from src.services.base import BaseService


class ProjectVersionService(BaseService):
    async def get_current_version(self, project_id: str):
        statement = (
            select(ProjectVersion)
            .where(ProjectVersion.project_id == project_id)
            .where(ProjectVersion.is_current_version == True)
        )
        current_version = (await self.session.exec(statement)).one_or_none()
        if not current_version:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"project version not found. project_id={project_id}",
            )
        return current_version
