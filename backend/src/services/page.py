from fastapi import HTTPException, status
from sqlmodel import col, desc, select, func
from src.models.dto.page import PageModel
from src.models.project import Page
from src.services.base import BaseService


class PageService(BaseService):
    async def get(self, page_id: str, current_version: str) -> Page:
        statement = (
            select(Page)
            .where(Page.page_id == page_id)
            .where(Page.current_version == current_version)
        )
        page = (await self.session.exec(statement)).one_or_none()
        if not page:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"page not found. page_id={page_id} current_version={current_version}",
            )
        return page

    async def get_all(
        self,
        project_id: str,
        current_version: str,
        name: str,
        current_page: int = 0,
        page_size: int = 10,
    ):
        statement = (
            select(Page)
            .where(Page.project_id == project_id)
            .where(Page.current_version == current_version)
        )
        if name:
            statement = statement.where(col(Page.name).like(f"%{name}%"))
        statement = statement.offset(current_page * page_size)
        statement = statement.limit(page_size)
        statement.order_by(desc(Page.created_at))

        total = (await self.session.exec(select(func.count()).select_from(Page))).one()
        pages = (await self.session.exec(statement)).all()

        return {"total": total, "pages": pages}

    async def create(
        self,
        tenant_id: str,
        project_id: str,
        current_version: str,
        page_model: PageModel,
    ):

        page = Page(
            name=page_model.name,
            project_id=project_id,
            tenant_id=tenant_id,
            current_version=current_version,
        )
        self.session.add(page)
        await self.session.flush()
        await self.session.commit()

    async def update(self, page_id: str, current_version: str, page_model: PageModel):
        page = await self.get(page_id=page_id, current_version=current_version)
        page_dict = page_model.model_dump()
        for name, value in page_dict.items():
            setattr(page, name, value)

        self.session.add(page)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(page)

    async def remove(self, page_id: str, current_version: str):
        page = await self.get(page_id, current_version)
        await self.session.delete(page)
        await self.session.flush()
        await self.session.commit()
