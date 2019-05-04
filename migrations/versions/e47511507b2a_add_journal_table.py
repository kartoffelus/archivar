"""add journal table

Revision ID: e47511507b2a
Revises: 8f912582b5f7
Create Date: 2019-05-04 15:29:02.789700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e47511507b2a'
down_revision = '8f912582b5f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journal',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_visible', sa.Boolean(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('edited_by_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], name=op.f('fk_journal_character_id_characters')),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], name=op.f('fk_journal_created_by_id_users')),
    sa.ForeignKeyConstraint(['edited_by_id'], ['users.id'], name=op.f('fk_journal_edited_by_id_users')),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], name=op.f('fk_journal_session_id_sessions')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_journal'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal')
    # ### end Alembic commands ###
