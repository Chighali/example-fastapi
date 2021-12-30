"""Add content to tabele

Revision ID: 37363ac7e79d
Revises: 71f56a777a14
Create Date: 2021-12-30 11:49:10.885835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37363ac7e79d'
down_revision = '71f56a777a14'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
