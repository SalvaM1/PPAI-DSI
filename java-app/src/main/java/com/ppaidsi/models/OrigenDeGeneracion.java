package com.ppaidsi.models;

public class OrigenDeGeneracion {

    private final String descripcion;
    private final String nombre;

    public OrigenDeGeneracion(String descripcion, String nombre) {
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


