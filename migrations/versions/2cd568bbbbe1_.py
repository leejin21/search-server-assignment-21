"""empty message

Revision ID: 2cd568bbbbe1
Revises: a9bfee46c75b
Create Date: 2022-01-10 13:20:42.021070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cd568bbbbe1'
down_revision = 'a9bfee46c75b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dogs', sa.Column('sex', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dogs', 'sex')
    # ### end Alembic commands ###