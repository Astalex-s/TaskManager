from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from AppTM.app.backend.db import Base
from AppTM.app.models import *


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


if __name__ in '__main__':
    from sqlalchemy.schema import CreateTable
    print(CreateTable(User.__table__))
