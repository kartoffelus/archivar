"""Add audit mixin -> new columns for everyone!

Revision ID: e58833710b6e
Revises: 77e07482a0b4
Create Date: 2019-04-14 21:17:12.170429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58833710b6e'
down_revision = '77e07482a0b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calendar_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('epochs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('event_categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('event_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))

    with op.batch_alter_table('map_node_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('map_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('maps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))

    with op.batch_alter_table('media_categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('media_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('months', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('moons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))

    with op.batch_alter_table('wiki_settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('edited', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('edited_by_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['created_by_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['edited_by_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wiki_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('edited')

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('parties', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('moons', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('months', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('media_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('media_categories', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_column('edited')
        batch_op.drop_column('created')

    with op.batch_alter_table('maps', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('map_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('map_node_types', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_column('edited')
        batch_op.drop_column('created')

    with op.batch_alter_table('event_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('event_categories', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('epochs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('created_by_id')

    with op.batch_alter_table('calendar_settings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('edited_by_id')
        batch_op.drop_column('edited')
        batch_op.drop_column('created_by_id')
        batch_op.drop_column('created')

    # ### end Alembic commands ###
