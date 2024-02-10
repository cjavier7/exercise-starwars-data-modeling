import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
""" 
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String (200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    favorites = relationship("Favorite_planet" ,backref="users")
    favorites_charc = relationship("Favorite_character", backref="users")
    favorites_vehic = relationship("Favorite_vehicle", backref="users")

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String (200), nullable=False)
    haircolor = Column(String(200), nullable=False)
    gender= Column(String(200), nullable=False)
    favorites = relationship("Favorite_Character", backref="characters")

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String (200), nullable=False)
    gravity= Column(String(200), nullable=False)
    favorites = relationship("Favorite_Planet", backref="planets")

class Vehicle (Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(200), nullable=False)
    favorites = relationship("Favorite_Vehicle", backref="vehicles")

class Favorite_Planet (Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_characters = Column(Integer, ForeignKey('planets.id'))


class Favorite_Vehicle (Base):
    __tablename__ =  'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_characters = Column(Integer, ForeignKey('vehicles.id'))


class Favorite_Character (Base):
    __tablename__ =  'favorites_characters'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_characters = Column(Integer, ForeignKey('characters.id'))






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
