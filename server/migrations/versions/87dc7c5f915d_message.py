"""message

Revision ID: 87dc7c5f915d
Revises: 6e7d8b26b785
Create Date: 2024-08-20 20:12:05.691163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87dc7c5f915d'
down_revision = '6e7d8b26b785'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventorys')
    with op.batch_alter_table('sales', schema=None) as batch_op:
        batch_op.drop_column('flavor')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales', schema=None) as batch_op:
        batch_op.add_column(sa.Column('flavor', sa.VARCHAR(), nullable=True))

    op.create_table('inventorys',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('pricePerBox', sa.INTEGER(), nullable=True),
    sa.Column('flavor', sa.VARCHAR(), nullable=True),
    sa.Column('stock', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_inventorys')
    )
    # ### end Alembic commands ###
