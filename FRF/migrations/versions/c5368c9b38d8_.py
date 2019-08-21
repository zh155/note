"""empty message

Revision ID: c5368c9b38d8
Revises: f48681d08eb9
Create Date: 2019-08-08 11:25:28.503865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5368c9b38d8'
down_revision = 'f48681d08eb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('city', sa.String(length=256), nullable=True),
    sa.Column('district', sa.String(length=256), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=256), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Integer(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cinema_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), nullable=True),
    sa.Column('city', sa.VARCHAR(length=256), nullable=True),
    sa.Column('district', sa.VARCHAR(length=256), nullable=True),
    sa.Column('address', sa.VARCHAR(length=256), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=256), nullable=True),
    sa.Column('score', sa.INTEGER(), nullable=True),
    sa.Column('hallnum', sa.INTEGER(), nullable=True),
    sa.Column('servicecharge', sa.INTEGER(), nullable=True),
    sa.Column('astrict', sa.INTEGER(), nullable=True),
    sa.Column('flag', sa.INTEGER(), nullable=True),
    sa.Column('isdelete', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('isdelete IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cinema')
    # ### end Alembic commands ###