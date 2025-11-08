from datetime import datetime
from .. import db

class EventoSismico(db.Model):
    __tablename__ = 'eventos'

    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_ocurrencia = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_hora_fin = db.Column(db.DateTime, nullable=True)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    magnitud = db.Column(db.Float, nullable=False)
    origen = db.Column(db.String(50), nullable=False)
    alcance = db.Column(db.Float, nullable=False)

    cambios_estado = db.relationship('CambioEstado', back_populates='evento', lazy='dynamic')
    series_temporales = db.relationship('SerieTemporal', back_populates='evento', lazy='dynamic')

    def __repr__(self):
        return f"<EventoSismico {self.id} - {self.magnitud}M>"


class Estado(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    ambito = db.Column(db.String(50), nullable=False)
    nombreEstado = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Estado {self.ambito}:{self.nombreEstado}>"


class CambioEstado(db.Model):
    __tablename__ = 'cambios_estado'

    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'), nullable=False)
    fecha_hora_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_hora_fin = db.Column(db.DateTime, nullable=True)

    evento = db.relationship('EventoSismico', back_populates='cambios_estado')
    estado = db.relationship('Estado')


class TipoDeDato(db.Model):
    __tablename__ = 'tipos_dato'

    id = db.Column(db.Integer, primary_key=True)
    nombreUnidadMedida = db.Column(db.String(50), nullable=False)
    denominacion = db.Column(db.String(20), nullable=False)
    valorUmbral = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<TipoDeDato {self.nombreUnidadMedida}>"


class SerieTemporal(db.Model):
    __tablename__ = 'series_temporales'

    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    condicion_alarma = db.Column(db.String(100))
    fecha_hora_inicio_registro_muestras = db.Column(db.DateTime)
    fecha_hora_registro = db.Column(db.DateTime)
    frecuencia_muestreo = db.Column(db.Integer)

    evento = db.relationship('EventoSismico', back_populates='series_temporales')
    muestras = db.relationship('MuestraSismica', back_populates='serie')


class MuestraSismica(db.Model):
    __tablename__ = 'muestras_sismicas'

    id = db.Column(db.Integer, primary_key=True)
    serie_id = db.Column(db.Integer, db.ForeignKey('series_temporales.id'), nullable=False)
    fecha_hora_muestra = db.Column(db.DateTime, default=datetime.utcnow)

    serie = db.relationship('SerieTemporal', back_populates='muestras')
    detalles = db.relationship('DetalleMuestraSismica', back_populates='muestra')


class DetalleMuestraSismica(db.Model):
    __tablename__ = 'detalles_muestra'

    id = db.Column(db.Integer, primary_key=True)
    muestra_id = db.Column(db.Integer, db.ForeignKey('muestras_sismicas.id'), nullable=False)
    estacion_id = db.Column(db.Integer, db.ForeignKey('estaciones_sismologicas.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    muestra = db.relationship('MuestraSismica', back_populates='detalles')
    estacion = db.relationship('EstacionSismologica')


class EstacionSismologica(db.Model):
    __tablename__ = 'estaciones_sismologicas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    provincia = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Estacion {self.nombre} ({self.provincia})>"


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.id} - {self.nombre}>"


class Sesion(db.Model):
    __tablename__ = 'sesiones'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship('Usuario')