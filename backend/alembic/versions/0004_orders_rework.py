"""update orders schema for multi item and payments

Revision ID: 0004
Revises: 0003
Create Date: 2025-06-09 00:30:00
"""

from alembic import op
import sqlalchemy as sa

revision = '0004'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('shop_id', sa.Integer(), sa.ForeignKey('shops.id')))
    op.add_column('orders', sa.Column('pickup_time', sa.DateTime(timezone=True)))
    op.add_column('orders', sa.Column('status', sa.String(), server_default='pending', nullable=False))
    op.add_column('orders', sa.Column('payment_intent_id', sa.String(), nullable=True))
    op.drop_column('orders', 'product_id')
    op.drop_column('orders', 'quantity')

    op.create_table(
        'order_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('order_id', sa.Integer(), sa.ForeignKey('orders.id'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.id'), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False, server_default='1'),
    )


def downgrade():
    op.drop_table('order_items')
    op.add_column('orders', sa.Column('quantity', sa.Integer(), nullable=False, server_default='1'))
    op.add_column('orders', sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.id'), nullable=False))
    op.drop_column('orders', 'payment_intent_id')
    op.drop_column('orders', 'status')
    op.drop_column('orders', 'pickup_time')
    op.drop_column('orders', 'shop_id')

