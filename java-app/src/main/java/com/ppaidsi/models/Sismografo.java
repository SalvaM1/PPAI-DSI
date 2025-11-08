package com.ppaidsi.models;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Sismografo {

    private final LocalDate fechaAdquisicion;
    private final int id;
    private final String numeroSerie;
    private final List<SerieTemporal> seriesTemporales;
    private final EstacionSismologica estacionSismologica;

    public Sismografo(LocalDate fechaAdquisicion, int id, String numeroSerie, EstacionSismologica estacionSismologica) {
        this(fechaAdquisicion, id, numeroSerie, estacionSismologica, new ArrayList<>());
    }

    public Sismografo(LocalDate fechaAdquisicion, int id, String numeroSerie, EstacionSismologica estacionSismologica, List<SerieTemporal> seriesTemporales) {
        this.fechaAdquisicion = fechaAdquisicion;
        this.id = id;
        this.numeroSerie = numeroSerie;
        this.estacionSismologica = estacionSismologica;
        this.seriesTemporales = new ArrayList<>(seriesTemporales);
    }

    public LocalDate getFechaAdquisicion() {
        return fechaAdquisicion;
    }

    public int getId() {
        return id;
    }

    public String getNumeroSerie() {
        return numeroSerie;
    }

    public List<SerieTemporal> getSeriesTemporales() {
        return Collections.unmodifiableList(seriesTemporales);
    }

    public EstacionSismologica getEstacionSismologica() {
        return estacionSismologica;
    }
}

