package com.ppaidsi.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SerieTemporal {

    private final boolean condicionAlarma;
    private final LocalDateTime fechaHoraInicioMuestras;
    private final LocalDateTime fechaHoraRegistro;
    private final double frecuenciaMuestreo;
    private final List<MuestraSismica> muestras;
    private EstacionSismologica estacion;

    public SerieTemporal(
            boolean condicionAlarma,
            LocalDateTime fechaHoraInicioMuestras,
            LocalDateTime fechaHoraRegistro,
            double frecuenciaMuestreo,
            List<MuestraSismica> muestras) {
        this.condicionAlarma = condicionAlarma;
        this.fechaHoraInicioMuestras = fechaHoraInicioMuestras;
        this.fechaHoraRegistro = fechaHoraRegistro;
        this.frecuenciaMuestreo = frecuenciaMuestreo;
        this.muestras = new ArrayList<>(muestras);
        this.estacion = null;
    }

    public boolean isCondicionAlarma() {
        return condicionAlarma;
    }

    public LocalDateTime getFechaHoraInicioMuestras() {
        return fechaHoraInicioMuestras;
    }

    public LocalDateTime getFechaHoraRegistro() {
        return fechaHoraRegistro;
    }

    public double getFrecuenciaMuestreo() {
        return frecuenciaMuestreo;
    }

    public List<MuestraSismica> getMuestras() {
        return Collections.unmodifiableList(muestras);
    }

    public EstacionSismologica getEstacion() {
        return estacion;
    }

    public EstacionSismologica esMiSismografo(List<Sismografo> sismografos) {
        return sismografos.stream()
                .filter(sismografo -> sismografo.getSeriesTemporales().contains(this))
                .map(Sismografo::getEstacionSismologica)
                .findFirst()
                .orElse(null);
    }

    public void asignarEstacion(EstacionSismologica estacion) {
        this.estacion = estacion;
    }
}

