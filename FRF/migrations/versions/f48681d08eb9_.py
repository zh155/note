"""empty message

Revision ID: f48681d08eb9
Revises: daaab85ae721
Create Date: 2019-08-08 11:24:44.495464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f48681d08eb9'
down_revision = 'daaab85ae721'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_model',
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
    op.drop_table('cinema_user_permission')
    op.drop_table('permissions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('p_name', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('p_name')
    )
    op.create_table('cinema_user_permission',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('cinema_user_id', sa.INTEGER(), nullable=True),
    sa.Column('cinema_permission_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['cinema_permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['cinema_user_id'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cinema_model')
    # ### end Alembic commands ###
