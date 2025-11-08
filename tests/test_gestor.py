import pytest
from app import create_app, db
from app.models.entidades import EventoSismico
from app.servicios.gestor import GestorSismos