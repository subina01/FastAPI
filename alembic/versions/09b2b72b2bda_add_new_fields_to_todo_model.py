"""Add new fields to Todo model

Revision ID: 09b2b72b2bda
Revises: 66f18f17f44f
Create Date: 2025-01-13 12:15:33.156411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09b2b72b2bda'
down_revision: Union[str, None] = '66f18f17f44f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
