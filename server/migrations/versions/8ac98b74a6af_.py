"""empty message

Revision ID: 8ac98b74a6af
Revises: 27468b058208
Create Date: 2016-03-20 16:46:21.853048

"""

# revision identifiers, used by Alembic.
revision = '8ac98b74a6af'
down_revision = '27468b058208'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'editorsSelection',
               existing_type=sa.INTEGER(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'editorsSelection',
               existing_type=sa.INTEGER(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    ### end Alembic commands ###
