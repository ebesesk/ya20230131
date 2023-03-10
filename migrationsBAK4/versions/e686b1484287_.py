"""empty message

Revision ID: e686b1484287
Revises: 
Create Date: 2023-03-03 22:30:22.051227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e686b1484287'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worked', sa.Column('wage', sa.String(), nullable=False))
    op.drop_constraint('uq_worked_year', 'worked', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_worked_year', 'worked', ['year', 'month', 'day', 'user_id'])
    op.drop_column('worked', 'wage')
    # ### end Alembic commands ###
