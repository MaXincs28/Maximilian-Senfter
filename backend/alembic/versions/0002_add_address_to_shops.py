"""add address column to shops

Revision ID: 0002
Revises: 0001
Create Date: 2025-06-09 00:10:00
"""

from alembic import op
import sqlalchemy as sa

revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('shops', sa.Column('address', sa.String(), nullable=True))


def downgrade():
    op.drop_column('shops', 'address')
