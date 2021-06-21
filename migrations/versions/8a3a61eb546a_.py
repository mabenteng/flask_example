"""empty message

Revision ID: 8a3a61eb546a
Revises: 96e86eb53b50
Create Date: 2021-06-21 14:21:24.920137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a3a61eb546a'
down_revision = '96e86eb53b50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('pwd', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vip')
    # ### end Alembic commands ###