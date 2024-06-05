import enum
from typing import Optional
import uuid

from sqlmodel import Field, text
from src.models.base import BaseSQLModel


class ProjectStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inacitve"
    DELETED = "deleted"


class Project(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    name: str
    description: Optional[str] = None
    status: ProjectStatus = ProjectStatus.ACTIVE


class ProjectVersion(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    name: str
    description: str
    is_current_version: bool


class Page(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    current_version: uuid.UUID

    page_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    name: str


class Element(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    current_version: uuid.UUID
    name: str
    selector: str
    target: str

    element_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )


class PageWithElement(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    current_version: uuid.UUID

    page_with_element_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )

    page_id: uuid.UUID
    element_id: uuid.UUID


class OperationType(str, enum.Enum):
    FOR = "for"
    IF = "if"
    DESC = "desc"


class Operation(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    page_id: uuid.UUID
    current_version: uuid.UUID

    operation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    description: str
    operation_type: OperationType
    parent_id: uuid.UUID


class Step(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    page_operation_id: uuid.UUID
    current_version: uuid.UUID
    command: str
    element_id: Optional[uuid.UUID] = None
    value: Optional[str] = None

    step_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )


class OperationChildType(str, enum.Enum):
    OPERATION = "operation"
    STEP = "step"


class OperationOrder(BaseSQLModel, table=True):
    operation_order_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    current_version: uuid.UUID
    operation_id: uuid.UUID
    children_id: uuid.UUID
    child_type: OperationChildType
    order_no: int


class Scenario(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID

    name: str
    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    current_version: uuid.UUID


class ScenarioPage(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    scenario_id: uuid.UUID
    scenario_page_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    page_id: uuid.UUID
    current_version: uuid.UUID
    order_no: int


class ScenarioPageOperation(BaseSQLModel, table=True):
    tenant_id: uuid.UUID
    project_id: uuid.UUID
    scenario_page_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
    )
    scenario_page_operation_id: uuid.UUID
    current_version: uuid.UUID
    operation_id: uuid.UUID
    order_no: int
