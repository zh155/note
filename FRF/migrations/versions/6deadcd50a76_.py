"""empty message

Revision ID: 6deadcd50a76
Revises: 904dd8274fb0
Create Date: 2019-07-27 23:42:20.394362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6deadcd50a76'
down_revision = '904dd8274fb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('phone', table_name='base_model')
    op.drop_index('username', table_name='base_model')
    op.drop_table('base_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_model',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('_password', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('is_delete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('permission', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'base_model', ['username'], unique=True)
    op.create_index('phone', 'base_model', ['phone'], unique=True)
    op.drop_table('user')
    # ### end Alembic commands ###
