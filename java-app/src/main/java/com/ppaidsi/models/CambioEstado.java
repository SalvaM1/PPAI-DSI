package com.ppaidsi.models;

import java.time.LocalDateTime;
import java.util.Objects;

public class CambioEstado {

    private final Estado estado;
    private final LocalDateTime fechaHoraInicio;
    private LocalDateTime fechaHoraFin;

    public CambioEstado(Estado estado, LocalDateTime fechaHoraInicio) {
        this(estado, fechaHoraInicio, null);
    }

    public CambioEstado(Estado estado, LocalDateTime fechaHoraInicio, LocalDateTime fechaHoraFin) {
        this.estado = Objects.requireNonNull(estado, "estado no puede ser nulo");
        this.fechaHoraInicio = Objects.requireNonNull(fechaHoraInicio, "fechaHoraInicio no puede ser nula");
        this.fechaHoraFin = fechaHoraFin;
    }

    public Estado getEstado() {
        return estado;
    }

    public LocalDateTime getFechaHoraInicio() {
        return fechaHoraInicio;
    }

    public LocalDateTime getFechaHoraFin() {
        return fechaHoraFin;
    }

    public void cerrar(LocalDateTime fechaHoraFin) {
        this.fechaHoraFin = Objects.requireNonNull(fechaHoraFin, "fechaHoraFin no puede ser nula");
    }

    @Override
    public String toString() {
        var fin = fechaHoraFin != null ? fechaHoraFin.toString() : "actual";
        return "Cambio a '" + estado + "' desde " + fechaHoraInicio + " hasta " + fin;
    }
}

