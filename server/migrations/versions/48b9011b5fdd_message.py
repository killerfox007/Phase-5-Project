"""message

Revision ID: 48b9011b5fdd
Revises: 557466b614ed
Create Date: 2024-08-08 15:28:11.863005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48b9011b5fdd'
down_revision = '557466b614ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_constraint('fk_locations_scout_id_scouts', type_='foreignkey')
        batch_op.drop_constraint('fk_locations_sale_id_sales', type_='foreignkey')
        batch_op.drop_column('scout_id')
        batch_op.drop_column('sale_id')

    with op.batch_alter_table('scouts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_scouts_location_id_locations', type_='foreignkey')
        batch_op.drop_constraint('fk_scouts_sale_id_sales', type_='foreignkey')
        batch_op.drop_column('location_id')
        batch_op.drop_column('sale_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scouts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sale_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('location_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_scouts_sale_id_sales', 'sales', ['sale_id'], ['id'])
        batch_op.create_foreign_key('fk_scouts_location_id_locations', 'locations', ['location_id'], ['id'])

    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sale_id', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('scout_id', sa.VARCHAR(), nullable=True))
        batch_op.create_foreign_key('fk_locations_sale_id_sales', 'sales', ['sale_id'], ['id'])
        batch_op.create_foreign_key('fk_locations_scout_id_scouts', 'scouts', ['scout_id'], ['id'])

    # ### end Alembic commands ###
