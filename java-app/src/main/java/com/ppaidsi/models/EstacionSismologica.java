package com.ppaidsi.models;

import java.time.LocalDate;

public class EstacionSismologica {

    private final String codigo;
    private final String documentoCertificacion;
    private final LocalDate fechaSolicitudCertificacion;
    private final double latitud;
    private final double longitud;
    private final String nombre;
    private final String numeroCertificacion;

    public EstacionSismologica(
            String codigo,
            String documentoCertificacion,
            LocalDate fechaSolicitudCertificacion,
            double latitud,
            double longitud,
            String nombre,
            String numeroCertificacion) {
        this.codigo = codigo;
        this.documentoCertificacion = documentoCertificacion;
        this.fechaSolicitudCertificacion = fechaSolicitudCertificacion;
        this.latitud = latitud;
        this.longitud = longitud;
        this.nombre = nombre;
        this.numeroCertificacion = numeroCertificacion;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getDocumentoCertificacion() {
        return documentoCertificacion;
    }

    public LocalDate getFechaSolicitudCertificacion() {
        return fechaSolicitudCertificacion;
    }

    public double getLatitud() {
        return latitud;
    }

    public double getLongitud() {
        return longitud;
    }

    public String getNombre() {
        return nombre;
    }

    public String getNumeroCertificacion() {
        return numeroCertificacion;
    }
}


