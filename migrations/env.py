from web_fastapi.config import (
    DB_DSN,
    DB_DRIVER_ALEMBIC,
    db_dsn_default,
    TESTING,
)
from web_fastapi.main import db, load_modules

from logging.config import fileConfig

from sqlalchemy.engine.url import URL, make_url
from sqlalchemy import engine_from_config, pool

from alembic import context
from starlette.config import Config

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)


def DB_DSN_ALEMBIC():
    config = Config()
    global db_dsn_default
    default = dict(**db_dsn_default)
    default["drivername"] = DB_DRIVER_ALEMBIC
    db_dsn_alembic = config(
        "DB_DSN_ALEMBIC",
        cast=make_url,
        default=URL(**default),
    )
    print(db_dsn_alembic)
    return str(db_dsn_alembic)

# 預設載入本地模組，讓 models.users 模型載入 init_app()
# 載入後 db 中也會有的元數據(sqlalchemy.Model.Base.metadata)，
# 拿著元數據可以進行遷移，比較等等。
load_modules()

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
# 指定 models.users 中的元數據(sqlalchemy.Model.Base.metadata)
target_metadata = db

# 如果不起用 TESTING 將載入 alembic.ini
if TESTING:
    config.set_main_option("sqlalchemy.url", DB_DSN_ALEMBIC())

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    print(url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
