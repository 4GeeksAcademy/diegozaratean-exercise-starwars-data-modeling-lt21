import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Estudio(Base):
    __tablename__ = 'estudio'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    logo = Column(String(250), nullable=False)
    slogan = Column(String(250), nullable=False)
			
class ModoJuego(Base):
    __tablename__ = 'modo_juego'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

class Videojuego(Base):
    __tablename__ = 'videojuego'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    año_lanzmaineto = Column(String(250), nullable=False)
    estudio_id = Column(Integer, ForeignKey('estudio.id'))
    estudio = relationship(Estudio)
    modo_juego_id = Column(Integer, ForeignKey('modo_juego.id'))
    modo_juego = relationship(ModoJuego)

class Consola(Base):
    __tablename__ = 'consola'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)


class VideojuegoConsola(Base):
    __tablename__ = 'videojuego_consola'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    consola_id = Column(Integer, ForeignKey('consola.id'))
    consola = relationship(Consola)
    videojuego_id = Column(Integer, ForeignKey('videojuego.id'))
    videojuego = relationship(Videojuego)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
