import os
import sys
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context

sys.path.append(os.getcwd())

from app.models.base import Base
from app.database import SQLALCHEMY_DATABASE_URL

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_engine(SQLALCHEMY_DATABASE_URL)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()