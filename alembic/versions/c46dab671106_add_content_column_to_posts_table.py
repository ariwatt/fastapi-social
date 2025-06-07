"""add content column to posts table

Revision ID: c46dab671106
Revises: 87b819bf7a88
Create Date: 2025-06-06 03:02:14.026126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c46dab671106'
down_revision: Union[str, None] = '87b819bf7a88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
