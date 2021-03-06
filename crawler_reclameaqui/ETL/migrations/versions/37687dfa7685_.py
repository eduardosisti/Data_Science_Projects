"""empty message

Revision ID: 37687dfa7685
Revises: 
Create Date: 2021-05-10 15:54:09.802969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37687dfa7685'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reclamacoes',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('titulo', sa.String(length=300), nullable=True),
    sa.Column('descricao', sa.String(length=5000), nullable=True),
    sa.Column('cidade', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.String(length=2), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('hora', sa.Time(), nullable=True),
    sa.Column('link', sa.String(length=200), nullable=False),
    sa.Column('dominio', sa.String(length=50), nullable=True),
    sa.Column('titulo_json', sa.JSON(), nullable=True),
    sa.Column('descricao_json', sa.JSON(), nullable=True),
    sa.Column('classes_titulo', sa.JSON(), nullable=True),
    sa.Column('classes_descricao', sa.JSON(), nullable=True),
    sa.Column('classes', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('link')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reclamacoes')
    # ### end Alembic commands ###
