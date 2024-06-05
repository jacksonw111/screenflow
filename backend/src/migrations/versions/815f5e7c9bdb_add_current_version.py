"""add current version

Revision ID: 815f5e7c9bdb
Revises: d8e273a5687f
Create Date: 2024-06-05 11:29:54.052720

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "815f5e7c9bdb"
down_revision: Union[str, None] = "d8e273a5687f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "page_with_elements",
        sa.Column("page_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
    )
    op.add_column(
        "page_with_elements",
        sa.Column("element_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("page_with_elements", "element_id")
    op.drop_column("page_with_elements", "page_id")
    # ### end Alembic commands ###