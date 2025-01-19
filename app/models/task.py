from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from AppTM.app.backend.db import Base
from AppTM.app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')


if __name__ in '__main__':
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Task.__table__))
