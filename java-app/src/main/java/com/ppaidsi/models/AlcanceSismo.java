package com.ppaidsi.models;

public class AlcanceSismo {

    private final String descripcion;
    private final String nombre;

    public AlcanceSismo(String descripcion, String nombre) {
        this.descripcion = descripcion;
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public String getNombre() {
        return nombre;
    }
}


