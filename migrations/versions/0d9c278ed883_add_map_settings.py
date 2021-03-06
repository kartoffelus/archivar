"""add map settings

Revision ID: 0d9c278ed883
Revises: 33840467da5b
Create Date: 2019-01-05 21:10:41.685836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d9c278ed883'
down_revision = '33840467da5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('map_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_change', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('no_wrap', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('map_settings', schema=None) as batch_op:
        batch_op.drop_column('no_wrap')
        batch_op.drop_column('last_change')

    # ### end Alembic commands ###
