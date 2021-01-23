"""start migrations

Revision ID: b194900de828
Revises: 
Create Date: 2021-01-22 20:35:03.259527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b194900de828"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "trades",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("accountAlias", sa.String(), nullable=True),
        sa.Column("accountId", sa.String(), nullable=True),
        sa.Column("assetCategory", sa.String(), nullable=True),
        sa.Column("buySell", sa.String(), nullable=True),
        sa.Column("conId", sa.String(), nullable=True),
        sa.Column("closePrice", sa.Float(), nullable=True),
        sa.Column("dateTime", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("expiry", sa.String(), nullable=True),
        sa.Column("fifoPnlRealized", sa.Float(), nullable=True),
        sa.Column("fxPnl", sa.Float(), nullable=True),
        sa.Column("ibCommission", sa.Float(), nullable=True),
        sa.Column("ibExecId", sa.String(), nullable=True),
        sa.Column("ibOrderId", sa.String(), nullable=True),
        sa.Column("mtmPnl", sa.Float(), nullable=True),
        sa.Column("multiplier", sa.Integer(), nullable=True),
        sa.Column("netCash", sa.Float(), nullable=True),
        sa.Column("openCloseIndicator", sa.String(), nullable=True),
        sa.Column("proceeds", sa.Float(), nullable=True),
        sa.Column("putCall", sa.String(), nullable=True),
        sa.Column("quantity", sa.Float(), nullable=True),
        sa.Column("strike", sa.String(), nullable=True),
        sa.Column("symbol", sa.String(), nullable=True),
        sa.Column("tradeDate", sa.String(), nullable=True),
        sa.Column("tradeId", sa.String(), nullable=True),
        sa.Column("tradePrice", sa.Float(), nullable=True),
        sa.Column("transactionId", sa.String(), nullable=True),
        sa.Column("underlyingSymbol", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("trades")
    # ### end Alembic commands ###