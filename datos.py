# datos.py
import random
from datetime import datetime, timedelta
from modelos import (
    EventoSismico,
    Estado,
    CambioEstado,
    SerieTemporal,
    MuestraSismica,
    DetalleMuestraSismica,
    TipoDeDato,
    Sismografo,
    EstacionSismologica
)



def crear_eventos():
    # ---- 1) Definir estados ----
    estado_pendiente = Estado('sismo', 'pendienteRevision')
    estado_revisado  = Estado('sismo', 'revisado')
    estado_bloqueado = Estado('sismo', 'bloqueado')

    # ---- 2) Definir tipos de dato ----
    tipo_longitud    = TipoDeDato('longitud', 'm',   0.0)
    tipo_frecuencia  = TipoDeDato('frecuencia', 'Hz', 0.0)
    tipo_velocidad   = TipoDeDato('velocidad de onda', 'm/s', 0.0)

    # ---- 3) Crear los eventos principales ----
    eventos = [
        EventoSismico(
            id=1,
            fecha_hora_fin        = datetime(2025,5,20,10,15),
            fecha_hora_ocurrencia = datetime(2025,5,20,10,0),
            latitud_epicentro     = -34.6,
            longitud_epicentro    = -58.4,
            latitud_hipocentro    = -34.7,
            longitud_hipocentro   = -58.5,
            valor_magnitud        = 5.4,
            clasificacion         = 'Moderado',
            magnitud              = 5.4,
            origen_generacion     = 'Tectónico',
            alcance               = 100
        ),
        EventoSismico(
            id=2,
            fecha_hora_fin        = datetime(2025,5,19, 9,15),
            fecha_hora_ocurrencia = datetime(2025,5,19, 8,45),
            latitud_epicentro     = -33.9,
            longitud_epicentro    = -60.2,
            latitud_hipocentro    = -34.0,
            longitud_hipocentro   = -60.3,
            valor_magnitud        = 4.8,
            clasificacion         = 'Leve',
            magnitud              = 4.8,
            origen_generacion     = 'Volcánico',
            alcance               = 50
        ),
        EventoSismico(
            id=3,
            fecha_hora_fin        = datetime(2025,5,17,12,30),
            fecha_hora_ocurrencia = datetime(2025,5,17,12,0),
            latitud_epicentro     = -35.0,
            longitud_epicentro    = -57.9,
            latitud_hipocentro    = -35.1,
            longitud_hipocentro   = -58.0,
            valor_magnitud        = 6.1,
            clasificacion         = 'Fuerte',
            magnitud              = 6.1,
            origen_generacion     = 'Tectónico',
            alcance               = 150
        )
    ]

    # ---- 4) Agregar cambios de estado iniciales ----
    for i, evento in enumerate(eventos):
        estado_actual = estado_pendiente if i < 2 else estado_revisado
        cambio = CambioEstado(
            estado             = estado_actual,
            fecha_hora_inicio  = evento.fecha_hora_ocurrencia
        )
        evento.agregar_cambio_estado(cambio)

    # ---- 5) Crear series temporales, muestras y detalles ----
    for evento in eventos:
        series = []
        # Hasta 2 series temporales por evento
        for s_idx in range(2):
            # Fecha de inicio de muestreo: desplazada s_idx minutos desde la ocurrencia
            inicio_muestreo = evento.fecha_hora_ocurrencia + timedelta(minutes=s_idx)
            registro_muestreo = inicio_muestreo + timedelta(seconds=0)
            frecuencia = 100.0 if s_idx == 0 else 50.0

            muestras = []
            # Hasta 2 muestras por serie
            for m_idx in range(2):
                timestamp_muestra = inicio_muestreo + timedelta(seconds=m_idx * 5)
                nroRandom = random.random()
                detalles = [
                    DetalleMuestraSismica(valor=round((0.1 * (s_idx+1) * (m_idx+1)) * nroRandom, 2), tipo_dato=tipo_longitud),
                    DetalleMuestraSismica(valor=round((1.0 * (s_idx+1) * (m_idx+1)) * nroRandom, 2), tipo_dato=tipo_frecuencia),
                    DetalleMuestraSismica(valor=round((500.0 * (s_idx+1) * (m_idx+1)) * nroRandom, 2), tipo_dato=tipo_velocidad)
                ]
                muestra = MuestraSismica(
                    fecha_hora_muestra = timestamp_muestra,
                    detalles           = detalles
                )
                muestras.append(muestra)

            serie = SerieTemporal(
                condicion_alarma           = False,
                fecha_hora_inicio_muestras = inicio_muestreo,
                fecha_hora_registro        = registro_muestreo,
                frecuencia_muestreo        = frecuencia,
                muestras                   = muestras
            )
            series.append(serie)

        # Asignar la lista de series al evento
        evento.series_temporales = series

        estaciones = [
        EstacionSismologica(
            codigo='ST-001',
            documentoCertificacion='cert_001.pdf',
            fechaSolicitudCertificacion=datetime(2024, 1, 10),
            latitud=-34.61,
            longitud=-58.38,
            nombre='Estación Central Buenos Aires',
            nroCertificacion='C-BA-001'
        ),
        EstacionSismologica(
            codigo='ST-002',
            documentoCertificacion='cert_002.pdf',
            fechaSolicitudCertificacion=datetime(2024, 2, 5),
            latitud=-33.92,
            longitud=-60.25,
            nombre='Estación Rosario Norte',
            nroCertificacion='C-RN-002'
        ),
        EstacionSismologica(
            codigo='ST-003',
            documentoCertificacion='cert_003.pdf',
            fechaSolicitudCertificacion=datetime(2024, 3, 15),
            latitud=-35.05,
            longitud=-57.95,
            nombre='Estación La Plata Sur',
            nroCertificacion='C-LP-003'
        )
    ]

    # ---- 7) Crear sismógrafos y asignarles series temporales y estaciones ----
    sismografos = []
    for i, evento in enumerate(eventos):
        sismografo = Sismografo(
            fechaAdquisicion=datetime(2023, 12, 1 + i),  # fechas distintas
            id=i + 1,
            nroSerie=f"SN-{1000 + i}",
            estacionSismologica=estaciones[i],  # uno a uno con estaciones
            seriesTemporales=evento.series_temporales  # ya están generadas
        )
        sismografos.append(sismografo)

    return eventos, estaciones, sismografos
