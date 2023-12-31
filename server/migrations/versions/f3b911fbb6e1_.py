"""empty message

Revision ID: f3b911fbb6e1
Revises: f46e977694b8
Create Date: 2023-11-22 16:02:41.997398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b911fbb6e1'
down_revision = 'f46e977694b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], name=op.f('fk_cart_items_cart_id_carts')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_cart_items_item_id_items')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_carts_item_id_items', type_='foreignkey')
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_carts_item_id_items', 'items', ['item_id'], ['id'])

    op.drop_table('cart_items')
    # ### end Alembic commands ###
