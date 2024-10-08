"""message

Revision ID: 557466b614ed
Revises: fb112b07c4c9
Create Date: 2024-08-07 22:11:14.572220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557466b614ed'
down_revision = 'fb112b07c4c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scout_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('sale_id', sa.String(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_locations_sale_id_sales'), 'sales', ['sale_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_locations_scout_id_scouts'), 'scouts', ['scout_id'], ['id'])

    with op.batch_alter_table('sales', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('scout_id', sa.String(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_sales_location_id_locations'), 'locations', ['location_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_sales_scout_id_scouts'), 'scouts', ['scout_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sales', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_sales_scout_id_scouts'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_sales_location_id_locations'), type_='foreignkey')
        batch_op.drop_column('scout_id')
        batch_op.drop_column('location_id')

    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_locations_scout_id_scouts'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_locations_sale_id_sales'), type_='foreignkey')
        batch_op.drop_column('sale_id')
        batch_op.drop_column('scout_id')

    # ### end Alembic commands ###
