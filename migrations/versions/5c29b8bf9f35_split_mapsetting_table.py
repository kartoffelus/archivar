"""split MapSetting table

Revision ID: 5c29b8bf9f35
Revises: fd67b6ffe895
Create Date: 2019-01-07 21:53:12.321545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c29b8bf9f35'
down_revision = 'fd67b6ffe895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min_zoom', sa.Integer(), nullable=True),
    sa.Column('max_zoom', sa.Integer(), nullable=True),
    sa.Column('default_zoom', sa.Integer(), nullable=True),
    sa.Column('tiles_path', sa.String(length=128), nullable=True),
    sa.Column('external_provider', sa.Boolean(), nullable=True),
    sa.Column('no_wrap', sa.Boolean(), nullable=True),
    sa.Column('last_change', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table(u'map_settings', schema=None) as batch_op:
        batch_op.drop_column('no_wrap')
        batch_op.drop_column('default_zoom')
        batch_op.drop_column('max_zoom')
        batch_op.drop_column('min_zoom')
        batch_op.drop_column('external_provider')
        batch_op.drop_column('last_change')
        batch_op.drop_column('tiles_path')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'map_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tiles_path', sa.VARCHAR(length=128), nullable=True))
        batch_op.add_column(sa.Column('last_change', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('external_provider', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('min_zoom', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('max_zoom', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('default_zoom', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('no_wrap', sa.BOOLEAN(), nullable=True))

    op.drop_table('maps')
    # ### end Alembic commands ###
