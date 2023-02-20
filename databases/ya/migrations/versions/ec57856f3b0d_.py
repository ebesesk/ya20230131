"""empty message

Revision ID: ec57856f3b0d
Revises: c33dc238969d
Create Date: 2023-02-17 16:02:31.455732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec57856f3b0d'
down_revision = 'c33dc238969d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_dislike',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_video_dislike_user_id_user')),
    sa.ForeignKeyConstraint(['video_id'], ['user.id'], name=op.f('fk_video_dislike_video_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'video_id', name=op.f('pk_video_dislike'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_dislike')
    # ### end Alembic commands ###
