"""add image column to products

Revision ID: 0003
Revises: 0002
Create Date: 2025-06-09 00:20:00
"""

from alembic import op
import sqlalchemy as sa

revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('products', sa.Column('image', sa.String(), nullable=True))


def downgrade():
    op.drop_column('products', 'image')
