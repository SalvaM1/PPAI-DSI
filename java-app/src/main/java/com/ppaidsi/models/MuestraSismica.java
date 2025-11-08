package com.ppaidsi.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MuestraSismica {

    private final LocalDateTime fechaHoraMuestra;
    private final List<DetalleMuestraSismica> detalles;

    public MuestraSismica(LocalDateTime fechaHoraMuestra) {
        this(fechaHoraMuestra, new ArrayList<>());
    }

    public MuestraSismica(LocalDateTime fechaHoraMuestra, List<DetalleMuestraSismica> detalles) {
        this.fechaHoraMuestra = fechaHoraMuestra;
        this.detalles = new ArrayList<>(detalles);
    }

    public LocalDateTime getFechaHoraMuestra() {
        return fechaHoraMuestra;
    }

    public List<DetalleMuestraSismica> getDetalles() {
        return Collections.unmodifiableList(detalles);
    }
}

