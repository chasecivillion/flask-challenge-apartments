"""create tables

Revision ID: 519f903b35fe
Revises: 
Create Date: 2023-04-11 10:35:14.993133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '519f903b35fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apartments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tenants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.Column('rent', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], ),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leases')
    op.drop_table('tenants')
    op.drop_table('apartments')
    # ### end Alembic commands ###
