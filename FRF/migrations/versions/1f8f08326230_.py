"""empty message

Revision ID: 1f8f08326230
Revises: c4dbc2918036
Create Date: 2019-08-08 11:59:04.210509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f8f08326230'
down_revision = 'c4dbc2918036'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cinemas', sa.Column('cinema_user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cinemas', 'cinema_user', ['cinema_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cinemas', type_='foreignkey')
    op.drop_column('cinemas', 'cinema_user_id')
    # ### end Alembic commands ###