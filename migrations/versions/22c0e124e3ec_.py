"""empty message

Revision ID: 22c0e124e3ec
Revises: None
Create Date: 2016-07-15 10:56:02.369728

"""

# revision identifiers, used by Alembic.
revision = '22c0e124e3ec'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('burials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sd_type', sa.String(), nullable=True),
    sa.Column('sd', sa.String(), nullable=True),
    sa.Column('lot', sa.String(), nullable=True),
    sa.Column('space', sa.String(), nullable=True),
    sa.Column('lot_owner', sa.String(), nullable=True),
    sa.Column('year_purch', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('birth_date', sa.String(), nullable=True),
    sa.Column('birth_place', sa.String(), nullable=True),
    sa.Column('death_date', sa.String(), nullable=True),
    sa.Column('age', sa.String(), nullable=True),
    sa.Column('death_place', sa.String(), nullable=True),
    sa.Column('death_cause', sa.String(), nullable=True),
    sa.Column('burial_date', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('more_notes', sa.String(), nullable=True),
    sa.Column('hidden_notes', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.Column('headstone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('burials')
    ### end Alembic commands ###
