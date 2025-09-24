import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Вариант проектирования таблиц с помощью ORM.
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True),
        server_default=sa.text("(CURRENT_TIMESTAMP AT TIME ZONE 'UTC')")
    )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True),
        server_default=sa.text("(CURRENT_TIMESTAMP AT TIME ZONE 'UTC')")
    )


# Вариант проектирования таблиц на чистом SQL.
users_table_script = """
    CREATE TABLE users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        username TEXT NOT NULL UNIQUE,
        created_at TIMESTAMPTZ NOT NULL DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'UTC')
    );
"""

messages_table_script = """
    CREATE TABLE messages (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        text TEXT NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'UTC')
    );
"""

user_id_index_script = "CREATE INDEX ix_messages_user_id ON messages (user_id);"


# Скрипт получения последнего сообщения каждого пользователя.
query = """
    SELECT m.id,
           m.user_id,
           m.text,
           m.created_at
    FROM messages m
    JOIN (
        SELECT user_id, MAX(created_at) AS last_created_at
        FROM messages
        GROUP BY user_id
    ) latest ON m.user_id = latest.user_id
            AND m.created_at = latest.last_created_at;
"""