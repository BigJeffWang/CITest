"""update TestCase column

Revision ID: 2edbc786a2a2
Revises: b409aed28399
Create Date: 2017-11-20 01:15:49.223054

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2edbc786a2a2'
down_revision = 'b409aed28399'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_case', sa.Column('permission_confirm', sa.Boolean(), nullable=True))
    op.add_column('test_case', sa.Column('response_confirm', sa.Boolean(), nullable=True))
    op.add_column('test_case', sa.Column('response_content', sa.Boolean(), nullable=True))
    op.add_column('test_case', sa.Column('token_confirm', sa.String(length=256), nullable=True))
    op.drop_column('test_case', 'response_status')
    op.drop_column('test_case', 'authen_token')
    op.drop_column('test_case', 'authen_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_case', sa.Column('authen_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('test_case', sa.Column('authen_token', mysql.VARCHAR(collation=u'utf8_bin', length=256), nullable=True))
    op.add_column('test_case', sa.Column('response_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('test_case', 'token_confirm')
    op.drop_column('test_case', 'response_content')
    op.drop_column('test_case', 'response_confirm')
    op.drop_column('test_case', 'permission_confirm')
    # ### end Alembic commands ###
