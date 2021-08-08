"""empty message

Revision ID: 199b5dc29e90
Revises: 2e113a51a06b
Create Date: 2021-08-08 15:03:36.260724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '199b5dc29e90'
down_revision = '2e113a51a06b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('media', sa.String(length=80), nullable=True),
    sa.Column('link', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('duration', sa.String(length=100), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('media_type', sa.String(length=100), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('media')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media')
    op.drop_table('album')
    # ### end Alembic commands ###
