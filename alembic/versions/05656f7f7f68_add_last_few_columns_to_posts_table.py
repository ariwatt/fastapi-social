"""add last few columns to posts table

Revision ID: 05656f7f7f68
Revises: a5c450c2f80b
Create Date: 2025-06-06 23:10:09.502288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05656f7f7f68'
down_revision: Union[str, None] = 'a5c450c2f80b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at",
                                     sa.TIMESTAMP(timezone=True),
                                     nullable=False,
                                     server_default=sa.text("NOW()")))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
