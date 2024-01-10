"""Add Chef Table and Relations

Revision ID: c94056377928
Revises: f45b916e263f
Create Date: 2023-11-24 08:26:05.477175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c94056377928'
down_revision: Union[str, None] = 'f45b916e263f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chefs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('recipes', sa.Column('chef_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipes', 'chefs', ['chef_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'chef_id')
    op.drop_table('chefs')
    # ### end Alembic commands ###