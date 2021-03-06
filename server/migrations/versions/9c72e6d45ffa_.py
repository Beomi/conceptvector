"""empty message

Revision ID: 9c72e6d45ffa
Revises: 4877b7a49c90
Create Date: 2016-03-20 08:33:31.513315

"""

# revision identifiers, used by Alembic.
revision = '9c72e6d45ffa'
down_revision = '4877b7a49c90'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'asset_id')
    # op.drop_column('articles', 'id')
    # op.drop_constraint(u'comments_assetID_fkey', 'comments', type_='foreignkey')
    # op.create_foreign_key(None, 'comments', 'articles', ['assetID'], ['url'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key(u'comments_assetID_fkey', 'comments', 'articles', ['assetID'], ['id'])
    op.add_column('articles', sa.Column('id', sa.INTEGER(), nullable=False))
    op.add_column('articles', sa.Column('asset_id', sa.INTEGER(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
