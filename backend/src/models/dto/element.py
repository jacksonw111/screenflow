import uuid
from sqlmodel import SQLModel


class ElementModel(SQLModel):
    page_id: str
    name: str
    selector: str
    target: str


class PageElementModel(SQLModel):
    page_id: str
    element_id: str


class PageWithElementResponseModel(SQLModel):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    current_version: uuid.UUID
    page_with_element_id: uuid.UUID
    page_id: uuid.UUID
    element_id: uuid.UUID

    page_name: str
