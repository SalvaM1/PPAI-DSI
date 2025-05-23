from datetime import datetime
from modelos import *

# Función para crear datos de prueba
def crear_eventos():
    # definir estados básicos
    estado_pendiente = Estado('sismo', 'pendienteRevision')
    estado_revisado = Estado('sismo', 'revisado')

    # crear eventos sin cambios aún
    eventos = [
        EventoSismico(
            fecha_hora_fin=datetime(2025,5,20,10,15),
            fecha_hora_ocurrencia=datetime(2025,5,20,10,0),
            latitud_epicentro=-34.6,
            longitud_epicentro=-58.4,
            latitud_hipocentro=-34.7,
            longitud_hipocentro=-58.5,
            valor_magnitud=5.4,
            clasificacion='Moderado',
            magnitud=5.4,
            origen_generacion='Tectónico',
            alcance=100
        ),
        EventoSismico(
            fecha_hora_fin=datetime(2025,5,19,9,15),
            fecha_hora_ocurrencia=datetime(2025,5,19,8,45),
            latitud_epicentro=-33.9,
            longitud_epicentro=-60.2,
            latitud_hipocentro=-34.0,
            longitud_hipocentro=-60.3,
            valor_magnitud=4.8,
            clasificacion='Leve',
            magnitud=4.8,
            origen_generacion='Volcánico',
            alcance=50
        ),
        EventoSismico(
            fecha_hora_fin=datetime(2025,5,17,12,30),
            fecha_hora_ocurrencia=datetime(2025,5,17,12,0),
            latitud_epicentro=-35.0,
            longitud_epicentro=-57.9,
            latitud_hipocentro=-35.1,
            longitud_hipocentro=-58.0,
            valor_magnitud=6.1,
            clasificacion='Fuerte',
            magnitud=6.1,
            origen_generacion='Tectónico',
            alcance=150
        )
    ]

    # asignar cambios de estado a los eventos
    for i, evento in enumerate(eventos):
        # para los dos primeros, estado pendienteRevision
        if i < 2:
            cambio = CambioEstado(fecha_hora_inicio=evento.fecha_hora_ocurrencia, estado=estado_pendiente)
        else:
            cambio = CambioEstado(fecha_hora_inicio=evento.fecha_hora_ocurrencia, estado=estado_revisado)
        evento.agregar_cambio_estado(cambio)

    return eventos