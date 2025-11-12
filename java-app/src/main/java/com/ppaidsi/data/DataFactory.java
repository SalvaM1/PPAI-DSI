package com.ppaidsi.data;

import com.ppaidsi.models.CambioEstado;
import com.ppaidsi.models.DetalleMuestraSismica;
import com.ppaidsi.models.Estado;
import com.ppaidsi.models.EstacionSismologica;
import com.ppaidsi.models.EventoSismico;
import com.ppaidsi.models.MuestraSismica;
import com.ppaidsi.models.SerieTemporal;
import com.ppaidsi.models.Sesion;
import com.ppaidsi.models.Sismografo;
import com.ppaidsi.models.TipoDeDato;
import com.ppaidsi.models.Usuario;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public final class DataFactory {

    private DataFactory() {
    }

    public static DatosIniciales crearDatos() {
        var estadoPendiente = new Estado("sismo", "pendienteRevision");
        var estadoRevisado = new Estado("sismo", "revisado");
        var estadoBloqueado = new Estado("sismo", "bloqueado");

        var tipoLongitud = new TipoDeDato("longitud", "m", 0.0);
        var tipoFrecuencia = new TipoDeDato("frecuencia", "Hz", 0.0);
        var tipoVelocidad = new TipoDeDato("velocidad de onda", "m/s", 0.0);

        var eventos = List.of(
                new EventoSismico(
                        1,
                        LocalDateTime.of(2025, 5, 20, 10, 15),
                        LocalDateTime.of(2025, 5, 20, 10, 0),
                        -34.6,
                        -58.4,
                        -34.7,
                        -58.5,
                        5.4,
                        "Moderado",
                        5.4,
                        "Tectónico",
                        100
                ),
                new EventoSismico(
                        2,
                        LocalDateTime.of(2025, 5, 19, 9, 15),
                        LocalDateTime.of(2025, 5, 19, 8, 45),
                        -33.9,
                        -60.2,
                        -34.0,
                        -60.3,
                        4.8,
                        "Leve",
                        4.8,
                        "Volcánico",
                        50
                ),
                new EventoSismico(
                        3,
                        LocalDateTime.of(2025, 5, 17, 12, 30),
                        LocalDateTime.of(2025, 5, 17, 12, 0),
                        -35.0,
                        -57.9,
                        -35.1,
                        -58.0,
                        6.1,
                        "Fuerte",
                        6.1,
                        "Tectónico",
                        150
                )
        );

        for (int i = 0; i < eventos.size(); i++) {
            var evento = eventos.get(i);
            var estadoActual = i < 2 ? estadoPendiente : estadoRevisado;
            evento.agregarCambioEstado(new CambioEstado(estadoActual, evento.getFechaHoraOcurrencia()));
        }

        var random = new Random(42);
        for (var evento : eventos) {
            var series = new ArrayList<SerieTemporal>();
            for (int sIdx = 0; sIdx < 2; sIdx++) {
                var inicioMuestreo = evento.getFechaHoraOcurrencia().plusMinutes(sIdx);
                var registroMuestreo = inicioMuestreo.plusSeconds(0);
                var frecuencia = sIdx == 0 ? 100.0 : 50.0;

                var muestras = new ArrayList<MuestraSismica>();
                for (int mIdx = 0; mIdx < 2; mIdx++) {
                    var timestamp = inicioMuestreo.plusSeconds(mIdx * 5L);
                    var nroRandom = random.nextDouble();
                    var detalles = List.of(
                            new DetalleMuestraSismica(redondear(0.1 * (sIdx + 1) * (mIdx + 1) * nroRandom), tipoLongitud),
                            new DetalleMuestraSismica(redondear(1.0 * (sIdx + 1) * (mIdx + 1) * nroRandom), tipoFrecuencia),
                            new DetalleMuestraSismica(redondear(500.0 * (sIdx + 1) * (mIdx + 1) * nroRandom), tipoVelocidad)
                    );
                    muestras.add(new MuestraSismica(timestamp, detalles));
                }

                series.add(new SerieTemporal(
                        false,
                        inicioMuestreo,
                        registroMuestreo,
                        frecuencia,
                        muestras
                ));
            }
            evento.setSeriesTemporales(series);
        }

        var estaciones = List.of(
                new EstacionSismologica(
                        "ST-001",
                        "cert_001.pdf",
                        LocalDate.of(2024, 1, 10),
                        -34.61,
                        -58.38,
                        "Estación Central Buenos Aires",
                        "C-BA-001"
                ),
                new EstacionSismologica(
                        "ST-002",
                        "cert_002.pdf",
                        LocalDate.of(2024, 2, 5),
                        -33.92,
                        -60.25,
                        "Estación Rosario Norte",
                        "C-RN-002"
                ),
                new EstacionSismologica(
                        "ST-003",
                        "cert_003.pdf",
                        LocalDate.of(2024, 3, 15),
                        -35.05,
                        -57.95,
                        "Estación La Plata Sur",
                        "C-LP-003"
                )
        );

        var sismografos = new ArrayList<Sismografo>();
        for (int i = 0; i < eventos.size(); i++) {
            var fechaAdquisicion = LocalDate.of(2023, 12, 1 + i);
            var sismografo = new Sismografo(
                    fechaAdquisicion,
                    i + 1,
                    "SN-" + (1000 + i),
                    estaciones.get(i),
                    eventos.get(i).getSeriesTemporales()
            );
            sismografos.add(sismografo);
        }

        sismografos.forEach(sismografo ->
                sismografo.getSeriesTemporales().forEach(serie ->
                        serie.asignarEstacion(sismografo.getEstacionSismologica())
                )
        );

        var usuarios = List.of(
                new Usuario("Juan", "actual"),
                new Usuario("Ana", "inactivo"),
                new Usuario("Pedro", "actual")
        );

        var sesiones = List.of(
                new Sesion(List.of(usuarios.get(0), usuarios.get(1)), 1),
                new Sesion(List.of(usuarios.get(2)), 2)
        );

        return new DatosIniciales(eventos, estaciones, sismografos, usuarios, sesiones, estadoBloqueado);
    }

    private static double redondear(double valor) {
        return Math.round(valor * 100.0) / 100.0;
    }

    public record DatosIniciales(
            List<EventoSismico> eventos,
            List<EstacionSismologica> estaciones,
            List<Sismografo> sismografos,
            List<Usuario> usuarios,
            List<Sesion> sesiones,
            Estado estadoBloqueado
    ) {
    }
}


