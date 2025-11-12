package com.ppaidsi.models;

public class Usuario {

    private final String nombre;
    private final String estado;

    public Usuario(String nombre, String estado) {
        this.nombre = nombre;
        this.estado = estado;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEstado() {
        return estado;
    }

    public boolean esActual() {
        return "actual".equalsIgnoreCase(estado);
    }
}


