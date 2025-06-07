"""add foreign-key to posts table

Revision ID: a5c450c2f80b
Revises: 0da38087efdb
Create Date: 2025-06-06 04:04:20.170840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5c450c2f80b'
down_revision: Union[str, None] = '0da38087efdb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk",
                          source_table="posts",
                          referent_table="users",
                          local_cols=["owner_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
