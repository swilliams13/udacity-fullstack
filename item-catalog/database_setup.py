import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email
        }


class Category(Base):

    __tablename__ = "category"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):

    __tablename__ = "item"

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category = relationship(Category)
    cat_id = Column(Integer, ForeignKey('category.id'))
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'cat_id': self.cat_id,
            'user_id': self.user_id,
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
