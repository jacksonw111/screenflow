"""account / tenant / project

Revision ID: 234fd4747a70
Revises: 
Create Date: 2024-06-03 10:25:19.191028

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "234fd4747a70"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accounts",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("password", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("password_salt", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "role",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default=sa.text("'user'::character varying"),
            nullable=True,
        ),
        sa.Column("last_login_at", sa.DateTime(), nullable=True),
        sa.Column("last_login_ip", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "last_active_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default=sa.text("'active'::character varying"),
            nullable=False,
        ),
        sa.Column("initialized_at", sa.DateTime(), nullable=True),
        sa.Column(
            "space_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("space_id"),
    )
    op.create_index(op.f("ix_accounts_email"), "accounts", ["email"], unique=True)
    op.create_index(op.f("ix_accounts_id"), "accounts", ["id"], unique=True)
    op.create_table(
        "elements",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "element_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_elements_element_id"), "elements", ["element_id"], unique=True
    )
    op.create_index(op.f("ix_elements_id"), "elements", ["id"], unique=True)
    op.create_table(
        "operation_orders",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "operation_order_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("operation_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("children_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "child_type",
            sa.Enum("OPERATION", "STEP", name="operationchildtype"),
            nullable=False,
        ),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_operation_orders_id"), "operation_orders", ["id"], unique=True
    )
    op.create_index(
        op.f("ix_operation_orders_operation_order_id"),
        "operation_orders",
        ["operation_order_id"],
        unique=True,
    )
    op.create_table(
        "operations",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("page_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "operation_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "operation_type",
            sa.Enum("FOR", "IF", "DESC", name="operationtype"),
            nullable=False,
        ),
        sa.Column("parent_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_operations_id"), "operations", ["id"], unique=True)
    op.create_index(
        op.f("ix_operations_operation_id"), "operations", ["operation_id"], unique=True
    )
    op.create_table(
        "page_with_elements",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "page_with_element_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_page_with_elements_id"), "page_with_elements", ["id"], unique=True
    )
    op.create_index(
        op.f("ix_page_with_elements_page_with_element_id"),
        "page_with_elements",
        ["page_with_element_id"],
        unique=True,
    )
    op.create_table(
        "pages",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "page_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_pages_id"), "pages", ["id"], unique=True)
    op.create_index(op.f("ix_pages_page_id"), "pages", ["page_id"], unique=True)
    op.create_table(
        "project_versions",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_project_versions_id"), "project_versions", ["id"], unique=True
    )
    op.create_table(
        "projects",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "status",
            sa.Enum("ACTIVE", "INACTIVE", "DELETED", name="projectstatus"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_projects_id"), "projects", ["id"], unique=True)
    op.create_table(
        "scenario_page_operations",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "scenario_page_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "scenario_page_operation_id", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("operation_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_scenario_page_operations_id"),
        "scenario_page_operations",
        ["id"],
        unique=True,
    )
    op.create_index(
        op.f("ix_scenario_page_operations_scenario_page_id"),
        "scenario_page_operations",
        ["scenario_page_id"],
        unique=True,
    )
    op.create_table(
        "scenario_pages",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("scenario_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "scenario_page_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("page_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_scenario_pages_id"), "scenario_pages", ["id"], unique=True)
    op.create_index(
        op.f("ix_scenario_pages_scenario_page_id"),
        "scenario_pages",
        ["scenario_page_id"],
        unique=True,
    )
    op.create_table(
        "scenarios",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "scenario_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_scenarios_id"), "scenarios", ["id"], unique=True)
    op.create_index(
        op.f("ix_scenarios_scenario_id"), "scenarios", ["scenario_id"], unique=True
    )
    op.create_table(
        "steps",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("project_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("page_operation_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "step_id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("current_version", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_steps_id"), "steps", ["id"], unique=True)
    op.create_index(op.f("ix_steps_step_id"), "steps", ["step_id"], unique=True)
    op.create_table(
        "tenant_account_joins",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("account_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "role",
            sa.Enum("ADMIN", "NORMAL", "GUEST", name="tenantaccountjoinrole"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_tenant_account_joins_id"), "tenant_account_joins", ["id"], unique=True
    )
    op.create_table(
        "tenants",
        sa.Column(
            "id",
            sqlmodel.sql.sqltypes.GUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "updated_by",
            sqlmodel.sql.sqltypes.AutoString(),
            server_default="admin",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("current_timestamp(0)"),
            nullable=False,
        ),
        sa.Column("owner_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("workspace", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tenants_id"), "tenants", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tenants_id"), table_name="tenants")
    op.drop_table("tenants")
    op.drop_index(op.f("ix_tenant_account_joins_id"), table_name="tenant_account_joins")
    op.drop_table("tenant_account_joins")
    op.drop_index(op.f("ix_steps_step_id"), table_name="steps")
    op.drop_index(op.f("ix_steps_id"), table_name="steps")
    op.drop_table("steps")
    op.drop_index(op.f("ix_scenarios_scenario_id"), table_name="scenarios")
    op.drop_index(op.f("ix_scenarios_id"), table_name="scenarios")
    op.drop_table("scenarios")
    op.drop_index(
        op.f("ix_scenario_pages_scenario_page_id"), table_name="scenario_pages"
    )
    op.drop_index(op.f("ix_scenario_pages_id"), table_name="scenario_pages")
    op.drop_table("scenario_pages")
    op.drop_index(
        op.f("ix_scenario_page_operations_scenario_page_id"),
        table_name="scenario_page_operations",
    )
    op.drop_index(
        op.f("ix_scenario_page_operations_id"), table_name="scenario_page_operations"
    )
    op.drop_table("scenario_page_operations")
    op.drop_index(op.f("ix_projects_id"), table_name="projects")
    op.drop_table("projects")
    op.drop_index(op.f("ix_project_versions_id"), table_name="project_versions")
    op.drop_table("project_versions")
    op.drop_index(op.f("ix_pages_page_id"), table_name="pages")
    op.drop_index(op.f("ix_pages_id"), table_name="pages")
    op.drop_table("pages")
    op.drop_index(
        op.f("ix_page_with_elements_page_with_element_id"),
        table_name="page_with_elements",
    )
    op.drop_index(op.f("ix_page_with_elements_id"), table_name="page_with_elements")
    op.drop_table("page_with_elements")
    op.drop_index(op.f("ix_operations_operation_id"), table_name="operations")
    op.drop_index(op.f("ix_operations_id"), table_name="operations")
    op.drop_table("operations")
    op.drop_index(
        op.f("ix_operation_orders_operation_order_id"), table_name="operation_orders"
    )
    op.drop_index(op.f("ix_operation_orders_id"), table_name="operation_orders")
    op.drop_table("operation_orders")
    op.drop_index(op.f("ix_elements_id"), table_name="elements")
    op.drop_index(op.f("ix_elements_element_id"), table_name="elements")
    op.drop_table("elements")
    op.drop_index(op.f("ix_accounts_id"), table_name="accounts")
    op.drop_index(op.f("ix_accounts_email"), table_name="accounts")
    op.drop_table("accounts")
    # ### end Alembic commands ###