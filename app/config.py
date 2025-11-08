import os

class Config:
    """
    Configuración base para la aplicación.
    """
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///sismos.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False