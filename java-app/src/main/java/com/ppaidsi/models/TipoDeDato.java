package com.ppaidsi.models;

public class TipoDeDato {

    private final String denominacion;
    private final String nombreUnidadMedida;
    private final double valorUmbral;

    public TipoDeDato(String denominacion, String nombreUnidadMedida, double valorUmbral) {
        this.denominacion = denominacion;
        this.nombreUnidadMedida = nombreUnidadMedida;
        this.valorUmbral = valorUmbral;
    }

    public String getDenominacion() {
        return denominacion;
    }

    public String getNombreUnidadMedida() {
        return nombreUnidadMedida;
    }

    public double getValorUmbral() {
        return valorUmbral;
    }
}


