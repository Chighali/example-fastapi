"""Add user table

Revision ID: 150ae4b58b2e
Revises: 37363ac7e79d
Create Date: 2021-12-30 11:59:37.837062

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150ae4b58b2e'
down_revision = '37363ac7e79d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UnicodeText('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
