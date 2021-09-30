"""baseline

Revision ID: 7f96858fc056
Revises: 
Create Date: 2021-09-30 13:01:49.568879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f96858fc056'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String, nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("idx_users_id"), "users", ["id"], unique=True)
    op.create_index(op.f("idx_users_email"), "users", ["email"], unique=True)
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String, nullable=True),
        sa.Column("author", sa.String, nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("idx_books_id"), "books", ["id"], unique=False)
    op.create_index(op.f("idx_books_author"), "books", ["author"], unique=False)


def downgrade():
    op.drop_index(op.f("idx_users_id"), table_name="users")
    op.drop_index(op.f("idx_users_email"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("idx_books_id"), table_name="books")
    op.drop_index(op.f("idx_books_author"), table_name="books")
    op.drop_table("books")
