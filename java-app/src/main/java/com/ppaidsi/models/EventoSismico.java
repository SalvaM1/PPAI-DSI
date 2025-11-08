package com.ppaidsi.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class EventoSismico {

    private final int id;
    private final LocalDateTime fechaHoraFin;
    private final LocalDateTime fechaHoraOcurrencia;
    private final double latitudEpicentro;
    private final double longitudEpicentro;
    private final double latitudHipocentro;
    private final double longitudHipocentro;
    private final double valorMagnitud;
    private final String clasificacion;
    private double magnitud;
    private String origenGeneracion;
    private double alcance;
    private final List<SerieTemporal> seriesTemporales;
    private final List<CambioEstado> cambiosEstado;

    public EventoSismico(
            int id,
            LocalDateTime fechaHoraFin,
            LocalDateTime fechaHoraOcurrencia,
            double latitudEpicentro,
            double longitudEpicentro,
            double latitudHipocentro,
            double longitudHipocentro,
            double valorMagnitud,
            String clasificacion,
            double magnitud,
            String origenGeneracion,
            double alcance) {
        this.id = id;
        this.fechaHoraFin = fechaHoraFin;
        this.fechaHoraOcurrencia = fechaHoraOcurrencia;
        this.latitudEpicentro = latitudEpicentro;
        this.longitudEpicentro = longitudEpicentro;
        this.latitudHipocentro = latitudHipocentro;
        this.longitudHipocentro = longitudHipocentro;
        this.valorMagnitud = valorMagnitud;
        this.clasificacion = clasificacion;
        this.magnitud = magnitud;
        this.origenGeneracion = origenGeneracion;
        this.alcance = alcance;
        this.seriesTemporales = new ArrayList<>();
        this.cambiosEstado = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public LocalDateTime getFechaHoraFin() {
        return fechaHoraFin;
    }

    public LocalDateTime getFechaHoraOcurrencia() {
        return fechaHoraOcurrencia;
    }

    public double getLatitudEpicentro() {
        return latitudEpicentro;
    }

    public double getLongitudEpicentro() {
        return longitudEpicentro;
    }

    public double getLatitudHipocentro() {
        return latitudHipocentro;
    }

    public double getLongitudHipocentro() {
        return longitudHipocentro;
    }

    public double getValorMagnitud() {
        return valorMagnitud;
    }

    public String getClasificacion() {
        return clasificacion;
    }

    public double getMagnitud() {
        return magnitud;
    }

    public void setMagnitud(double magnitud) {
        this.magnitud = magnitud;
    }

    public String getOrigenGeneracion() {
        return origenGeneracion;
    }

    public void setOrigenGeneracion(String origenGeneracion) {
        this.origenGeneracion = origenGeneracion;
    }

    public double getAlcance() {
        return alcance;
    }

    public void setAlcance(double alcance) {
        this.alcance = alcance;
    }

    public List<SerieTemporal> getSeriesTemporales() {
        return Collections.unmodifiableList(seriesTemporales);
    }

    public void setSeriesTemporales(List<SerieTemporal> nuevasSeries) {
        seriesTemporales.clear();
        seriesTemporales.addAll(nuevasSeries);
    }

    public void agregarSerieTemporal(SerieTemporal serieTemporal) {
        seriesTemporales.add(serieTemporal);
    }

    public void agregarCambioEstado(Estado estado) {
        var cambio = new CambioEstado(estado, LocalDateTime.now());
        cambiosEstado.add(cambio);
    }

    public void agregarCambioEstado(CambioEstado cambioEstado) {
        cambiosEstado.add(cambioEstado);
    }

    public Optional<Estado> obtenerEstadoActual() {
        if (cambiosEstado.isEmpty()) {
            return Optional.empty();
        }
        return Optional.ofNullable(cambiosEstado.get(cambiosEstado.size() - 1).getEstado());
    }

    public List<CambioEstado> getCambiosEstado() {
        return Collections.unmodifiableList(cambiosEstado);
    }
}

