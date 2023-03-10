"""empty message

Revision ID: 1af6c56e5a16
Revises: 4f8d3b22b160
Create Date: 2023-02-17 16:39:49.302196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1af6c56e5a16'
down_revision = '4f8d3b22b160'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video_dislike', schema=None) as batch_op:
        batch_op.drop_constraint('fk_video_dislike_video_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_video_dislike_video_id_video'), 'video', ['video_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video_dislike', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_video_dislike_video_id_video'), type_='foreignkey')
        batch_op.create_foreign_key('fk_video_dislike_video_id_user', 'user', ['video_id'], ['id'])

    # ### end Alembic commands ###
