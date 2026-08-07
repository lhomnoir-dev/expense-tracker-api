"""fix categories and expenses schema

Revision ID: 5b50a115ae4b
Revises: a50a47623918
Create Date: 2026-08-07 14:55:36.237617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b50a115ae4b'
down_revision: Union[str, Sequence[str], None] = 'a50a47623918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "categories",
        "owner_id",
        existing_type=sa.Integer(),
        nullable=True,
    )

    op.drop_constraint(
        "expenses_category_id_fkey",
        "expenses",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "expenses_category_id_fkey",
        "expenses",
        "categories",
        ["category_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "categories",
        "owner_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    op.drop_constraint(
        "expenses_category_id_fkey",
        "expenses",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "expenses_category_id_fkey",
        "expenses",
        "users",
        ["category_id"],
        ["id"],
    )
