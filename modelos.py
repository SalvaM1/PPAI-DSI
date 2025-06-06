# modelos.py
from datetime import datetime
from flask import render_template


class EventoSismico:
    def __init__(self, id, fecha_hora_fin, fecha_hora_ocurrencia,
                 latitud_epicentro, longitud_epicentro,
                 latitud_hipocentro, longitud_hipocentro,
                 valor_magnitud, clasificacion, magnitud,
                 origen_generacion, alcance):
        self.id = id
        self.fecha_hora_fin = fecha_hora_fin
        self.fecha_hora_ocurrencia = fecha_hora_ocurrencia
        self.latitud_epicentro = latitud_epicentro
        self.longitud_epicentro = longitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
        self.clasificacion = clasificacion
        self.magnitud = magnitud
        self.origen_generacion = origen_generacion
        self.alcance = alcance
        self.series_temporales = []

        # Lista de cambios de estado
        self.cambios_estado = []

    def agregar_cambio_estado(self, estado):
        self.cambios_estado.append(estado)

    def obtener_estado_actual(self):
        """
        Devuelve siempre una instancia de Estado:
         - Si el último elemento es un CambioEstado, extrae su .estado
         - Si ya es un Estado, lo devuelve directamente
        """
        if not self.cambios_estado:
            return None

        ultimo = self.cambios_estado[-1]
        # Importa la clase para evitar problemas circulares
        from modelos import CambioEstado

        if isinstance(ultimo, CambioEstado):
            return ultimo.estado
        else:
            return ultimo
    
class Estado:
    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado

    def __str__(self):
        return f"{self.ambito} - {self.nombre_estado}"

class CambioEstado:
    def __init__(self, estado, fecha_hora_inicio, fecha_hora_fin=None):
        self.estado = estado  # instancia de Estado
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin

    def __str__(self):
        fin = self.fecha_hora_fin if self.fecha_hora_fin else "actual"
        return f"Cambio a '{self.estado}' desde {self.fecha_hora_inicio} hasta {fin}"

class ClasificacionSismo:
    def __init__(self, km_desde, km_hasta, nombre):
        self.km_profundidad_desde = km_desde
        self.km_profundidad_hasta = km_hasta
        self.nombre = nombre

class MagnitudRichter:
    def __init__(self, descripcion, numero):
        self.descripcion_magnitud = descripcion
        self.numero = numero

class OrigenDeGeneracion:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

class AlcanceSismo:
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

class TipoDeDato:
    def __init__(self, denominacion, unidad_medida, valor_umbral):
        self.denominacion = denominacion
        self.nombre_unidad_medida = unidad_medida
        self.valor_umbral = valor_umbral

class DetalleMuestraSismica:
    def __init__(self, valor, tipo_dato):
        self.valor = valor
        self.tipo_dato = tipo_dato

class MuestraSismica:
    def __init__(self, fecha_hora_muestra, detalles=[]):
        self.fecha_hora_muestra = fecha_hora_muestra
        self.detalles = detalles  # lista de DetalleMuestraSismica

class SerieTemporal:
    def __init__(self, condicion_alarma,
                 fecha_hora_inicio_muestras,
                 fecha_hora_registro,
                 frecuencia_muestreo,
                 muestras=[]):
        self.condicion_alarma = condicion_alarma
        self.fecha_hora_inicio_muestras = fecha_hora_inicio_muestras
        self.fecha_hora_registro = fecha_hora_registro
        self.frecuencia_muestreo = frecuencia_muestreo
        self.muestras = muestras  # lista de MuestraSismica

    def esMiSismografo(self, sismografos):
        for sismografo in sismografos:
            if self in sismografo.series_temporales:
                return sismografo.estacion_sismologica
        return None



class Sismografo:
    def __init__(self, fechaAdquisicion, id, nroSerie, estacionSismologica, seriesTemporales=[]):   
        self.fecha_adquisicion = fechaAdquisicion
        self.id = id
        self.numero_serie = nroSerie
        self.series_temporales = seriesTemporales # lista de SerieTemporal
        self.estacion_sismologica = estacionSismologica # instancia de EstacionSismologica
        

class EstacionSismologica:
    def __init__(self, codigo, documentoCertificacion, fechaSolicitudCertificacion, latitud, longitud, nombre, nroCertificacion):
        self.codigo = codigo
        self.documento_certificacion = documentoCertificacion
        self.fecha_solicitud_certificacion = fechaSolicitudCertificacion
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
        self.numero_certificacion = nroCertificacion



class Interfaz:
    def mostrar_eventos(self, eventos):
        from flask import render_template
        return render_template('eventos.html', eventos=eventos)

    def habilitarVentana(self):
        return render_template('index.html')
    
    def mostrarEventoSeleccionado(self, evento, usuarios_activos):
        return render_template('evento_detalle.html', e=evento, usuario=usuarios_activos)
    
    
class Usuario:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado
    
    def esActual(self):
        return self.estado == "actual"




class Sesion:
    def __init__(self, usuarios, id):
        self.usuarios = usuarios  # instancia de Usuario
        self.id = id
        

    def buscarUsuario(self):
        # Devuelve el primer usuario activo
        for usuario in self.usuarios:
            if usuario.esActual():
                return usuario
        return None
    
    def es_usuario_actual(self):
        return any(usuarios.esActual() for usuarios in self.usuarios)
    

    
