# modelos.py

class EventoSismico:
    def __init__(self, fecha_hora_fin, fecha_hora_ocurrencia,
                 latitud_epicentro, longitud_epicentro,
                 latitud_hipocentro, longitud_hipocentro,
                 valor_magnitud, clasificacion, magnitud,
                 origen_generacion, alcance):
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
