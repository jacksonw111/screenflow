from typing import Annotated
from fastapi import APIRouter, Depends, Request

from src.models.dto.page import PageModel
from src.services.page import PageService


api = APIRouter(prefix="/pages")


@api.get("")
async def get_all(
    service: Annotated[PageService, Depends()],
    request: Request,
    name: str = None,
    current_page: int = 0,
    page_size: int = 10,
):
    return await service.get_all(
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
        name=name,
        current_page=current_page,
        page_size=page_size,
    )


@api.post("")
async def create(
    service: Annotated[PageService, Depends()], page: PageModel, request: Request
):
    await service.create(
        page_model=page,
        tenant_id=request.state.tenant_id,
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
    )


@api.put("/{page_id}")
async def update(
    service: Annotated[PageService, Depends()],
    page_id: str,
    page: PageModel,
    request: Request,
):
    await service.update(
        page_id=page_id,
        current_version=request.state.current_version_id,
        page_model=page,
    )


@api.delete("/{page_id}")
async def remove(
    service: Annotated[PageService, Depends()],
    page_id: str,
    request: Request,
):
    await service.remove(
        page_id=page_id, current_version=request.state.current_version_id
    )
