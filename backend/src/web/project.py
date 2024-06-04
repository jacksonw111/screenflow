from typing import Annotated
from fastapi import APIRouter, Depends, Request
from redis import Redis

from src.extensions import Extensions
from src.models.dto.project import ProjectModel
from src.services.Project import ProjectService
from src.services.project_version import ProjectVersionService


api = APIRouter(prefix="/projects")


@api.get("")
async def get_all(
    service: Annotated[ProjectService, Depends()],
    request: Request,
    name: str = None,
    current_page: int = 0,
    page_size: int = 10,
):
    return await service.get_all(
        tenant_id=request.state.tenant_id,
        name=name,
        current_page=current_page,
        page_size=page_size,
    )


@api.post("")
async def create(
    service: Annotated[ProjectService, Depends()],
    project: ProjectModel,
    request: Request,
):
    await service.create(project=project, tenant_id=request.state.tenant_id)


@api.get("/{project_id}")
async def setup(
    project_id: str,
    project_service: Annotated[ProjectService, Depends()],
    service: Annotated[ProjectVersionService, Depends()],
    redis: Annotated[Redis, Depends(Extensions.redis)],
):
    """
    对每一个请求锁定唯一的 version
    """
    project = await project_service.get_by_id(project_id)
    current_version = await service.get_current_version(project_id)
    await redis.set(str(project.id), str(current_version.id))


@api.put("/{project_id}")
async def update(
    service: Annotated[ProjectService, Depends()],
    project: ProjectModel,
    project_id: str,
):
    await service.update(project_id, project)


@api.delete("/{project_id}")
async def remove(
    service: Annotated[ProjectService, Depends()],
    project_id: str,
):
    await service.remove(project_id)
