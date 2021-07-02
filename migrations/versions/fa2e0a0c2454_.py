"""empty message

Revision ID: fa2e0a0c2454
Revises: 60ef9e526b0d
Create Date: 2021-07-02 15:46:01.983516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa2e0a0c2454'
down_revision = '60ef9e526b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Publicaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=1020), nullable=True),
    sa.Column('UUID', sa.String(length=36), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Publicaciones_timestamp'), 'Publicaciones', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Publicaciones_timestamp'), table_name='Publicaciones')
    op.drop_table('Publicaciones')
    # ### end Alembic commands ###

