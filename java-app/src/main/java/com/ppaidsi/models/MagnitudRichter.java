package com.ppaidsi.models;

public class MagnitudRichter {

    private final String descripcionMagnitud;
    private final double numero;

    public MagnitudRichter(String descripcionMagnitud, double numero) {
        this.descripcionMagnitud = descripcionMagnitud;
        this.numero = numero;
    }

    public String getDescripcionMagnitud() {
        return descripcionMagnitud;
    }

    public double getNumero() {
        return numero;
    }
}

