"""replace location geometry with numeric lat/lng

Revision ID: 0005
Revises: 0004
Create Date: 2025-06-09 00:40:00
"""

from alembic import op
import sqlalchemy as sa

revision = '0005'
down_revision = '0004'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('shops', 'location')
    op.add_column('shops', sa.Column('lat', sa.Numeric(9, 6), nullable=True))
    op.add_column('shops', sa.Column('lng', sa.Numeric(9, 6), nullable=True))


def downgrade():
    op.drop_column('shops', 'lng')
    op.drop_column('shops', 'lat')
    op.add_column('shops', sa.Column('location', sa.types.NullType))
