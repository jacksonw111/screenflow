from typing import Annotated
from fastapi import APIRouter, Depends, Request

from src.models.dto.element import ElementModel
from src.services.page_element import PageElementService


api = APIRouter(prefix="/page-elements")


@api.post("")
async def create(
    service: Annotated[PageElementService, Depends()],
    request: Request,
    element_model: ElementModel,
):
    await service.create(
        tenant_id=request.state.tenant_id,
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
        element_model=element_model,
    )


@api.get("")
async def get_all(
    service: Annotated[PageElementService, Depends()],
    request: Request,
    page_id: str = None,
    name: str = None,
):
    return await service.get_all(
        current_version=request.state.current_version_id,
        project_id=request.state.project_id,
        page_id=page_id,
        name=name,
    )


@api.put("/{element_id}")
async def update(
    service: Annotated[PageElementService, Depends()],
    request: Request,
    element_model: ElementModel,
    element_id: str,
):
    return await service.update(
        current_version=request.state.current_version_id,
        element_id=element_id,
        element_model=element_model,
    )


@api.get("/{element_id}/pages")
async def get(
    service: Annotated[PageElementService, Depends()],
    request: Request,
    element_id: str,
):
    return await service.get_all_pages(
        current_version=request.state.current_version_id,
        element_id=element_id,
    )


@api.post("{element_id}/{page_id}")
async def add_page(
    service: Annotated[PageElementService, Depends()],
    request: Request,
    page_id: str,
    element_id: str,
):
    await service.add_page_id(
        tenant_id=request.state.tenant_id,
        project_id=request.state.project_id,
        current_version=request.state.current_version_id,
        page_id=page_id,
        element_id=element_id,
    )
