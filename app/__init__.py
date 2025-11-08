from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Instancia global de la extensión de base de datos
db = SQLAlchemy()

def create_app():
    """
    Crea y configura la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Registrar blueprints
    from .rutas.eventos import eventos_bp
    app.register_blueprint(eventos_bp, url_prefix='/eventos')

    return app