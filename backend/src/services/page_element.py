import logging
from fastapi import HTTPException, status
from sqlmodel import and_, desc, select, delete
from src.models.dto.element import ElementModel, PageWithElementResponseModel
from src.models.project import Element, Page, PageWithElement
from src.services.base import BaseService


class PageElementService(BaseService):
    async def create(
        self,
        tenant_id: str,
        project_id: str,
        current_version: str,
        element_model: ElementModel,
    ):
        async with self.session.begin():
            element = Element(
                tenant_id=tenant_id,
                project_id=project_id,
                current_version=current_version,
                name=element_model.name,
                selector=element_model.selector,
                target=element_model.target,
            )
            self.session.add(element)
            await self.session.flush()

            page_with_element = PageWithElement(
                project_id=project_id,
                tenant_id=tenant_id,
                current_version=current_version,
                page_id=element_model.page_id,
                element_id=element.element_id,
            )
            self.session.add(page_with_element)
            await self.session.flush()
            await self.session.commit()

    async def get_all(
        self,
        current_version: str,
        project_id: str,
        page_id: str = None,
        name: str = None,
    ):
        statement = select(Element)
        if page_id:
            statement = select(Element).join(
                PageWithElement,
                and_(
                    PageWithElement.page_id == page_id,
                    PageWithElement.element_id == Element.element_id,
                    PageWithElement.current_version == current_version,
                ),
            )
        if name:
            statement = statement.where(Element.name == name)
        statement = statement.where(
            and_(
                Element.project_id == project_id,
                Element.current_version == current_version,
            )
        )
        statement.order_by(desc(Element.created_at))

        logging.info(statement)
        return (await self.session.exec(statement)).all()

    async def get_all_pages(self, element_id: str, current_version: str):
        statement = (
            select(
                PageWithElement,
                Page.name,
            )
            .join(
                Page,
                and_(
                    PageWithElement.page_id == Page.page_id,
                ),
                isouter=True,
            )
            .where(
                and_(
                    PageWithElement.element_id == element_id,
                    PageWithElement.current_version == current_version,
                )
            )
        )
        logging.info(statement)
        pages = (await self.session.exec(statement)).all()
        return [
            PageWithElementResponseModel(**page[0].model_dump(), page_name=page[1])
            for page in pages
        ]

    async def add_page_id(
        self,
        tenant_id: str,
        project_id: str,
        current_version: str,
        page_id: str,
        element_id: str,
    ):
        page_with_element = PageWithElement(
            project_id=project_id,
            tenant_id=tenant_id,
            current_version=current_version,
            page_id=page_id,
            element_id=element_id,
        )
        self.session.add(page_with_element)
        await self.session.flush()
        await self.session.commit()

    async def remove_page_id(
        self,
        page_with_element_id: str,
        current_version: str,
    ):
        page_with_element = await self.get_page_with_element(
            page_with_element_id=page_with_element_id, current_version=current_version
        )
        await self.session.delete(page_with_element)
        await self.session.flush()
        await self.session.commit()

    async def get_page_with_element(
        self, page_with_element_id: str, current_version: str
    ):
        page_with_element = (
            await self.session.exec(
                select(PageWithElement).where(
                    and_(
                        PageWithElement.page_with_element_id == page_with_element_id,
                        PageWithElement.current_version == current_version,
                    )
                )
            )
        ).one_or_none()

        if not page_with_element:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"""
                page with element related not found.
                page_with_element_id = {page_with_element_id},
                current_version = {current_version}""",
            )
        return page_with_element

    async def get(self, element_id: str, current_version: str):
        element = (
            await self.session.exec(
                select(Element).where(
                    and_(
                        Element.element_id == element_id,
                        Element.current_version == current_version,
                    )
                )
            )
        ).one_or_none()
        if not element:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"""
                element not found. element_id={element_id}, current_version = {current_version}
                """,
            )

        return element

    async def update(
        self, element_id: str, current_version: str, element_model: ElementModel
    ):
        element = await self.get(element_id=element_id, current_version=current_version)
        element_dict = element_model.model_dump()
        for name, value in element_dict.items():
            setattr(element, name, value)
        self.session.add(element)
        await self.session.flush()
        await self.session.commit()
        await self.session.refresh(element)

    async def remove(self, element_id: str, current_version: str, page_id: str):
        async with self.session.begin():
            await self.session.exec(
                delete(Element).where(
                    and_(
                        Element.element_id == element_id,
                        Element.current_version == current_version,
                    )
                )
            )

            await self.session.exec(
                delete(PageWithElement).where(
                    and_(
                        PageWithElement.page_id == page_id,
                        PageWithElement.element_id == element_id,
                        PageWithElement.current_version == current_version,
                    )
                )
            )
            await self.session.flush()
            await self.session.commit()
