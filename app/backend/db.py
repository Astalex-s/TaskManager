from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Создаем движок для базы данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# Создаем локальную сессию (сввязь с движком)
SessionLocal = sessionmaker(bind=engine)


# Создаем класс базы данных и наследуем его от DeclarativeBase
class Base(DeclarativeBase):
    pass
