"""made a change to the post model

Revision ID: 564971fb394a
Revises: 310a4598bf70
Create Date: 2020-02-24 14:12:20.588195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564971fb394a'
down_revision = '310a4598bf70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_created')
    # ### end Alembic commands ###
