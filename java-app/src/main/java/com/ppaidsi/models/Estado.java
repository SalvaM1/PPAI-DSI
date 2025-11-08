package com.ppaidsi.models;

import java.util.Objects;

public class Estado {

    private final String ambito;
    private final String nombreEstado;

    public Estado(String ambito, String nombreEstado) {
        this.ambito = Objects.requireNonNull(ambito, "ambito no puede ser nulo");
        this.nombreEstado = Objects.requireNonNull(nombreEstado, "nombreEstado no puede ser nulo");
    }

    public String getAmbito() {
        return ambito;
    }

    public String getNombreEstado() {
        return nombreEstado;
    }

    @Override
    public String toString() {
        return ambito + " - " + nombreEstado;
    }
}

