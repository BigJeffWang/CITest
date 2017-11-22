"""update TestCase column5

Revision ID: 622c3af67142
Revises: 7970b7d3f6e3
Create Date: 2017-11-20 01:43:31.822792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '622c3af67142'
down_revision = '7970b7d3f6e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_case', sa.Column('response_content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test_case', 'response_content')
    # ### end Alembic commands ###
