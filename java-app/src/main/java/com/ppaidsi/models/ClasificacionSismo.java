package com.ppaidsi.models;

public class ClasificacionSismo {

    private final double kmProfundidadDesde;
    private final double kmProfundidadHasta;
    private final String nombre;

    public ClasificacionSismo(double kmProfundidadDesde, double kmProfundidadHasta, String nombre) {
        this.kmProfundidadDesde = kmProfundidadDesde;
        this.kmProfundidadHasta = kmProfundidadHasta;
        this.nombre = nombre;
    }

    public double getKmProfundidadDesde() {
        return kmProfundidadDesde;
    }

    public double getKmProfundidadHasta() {
        return kmProfundidadHasta;
    }

    public String getNombre() {
        return nombre;
    }
}


