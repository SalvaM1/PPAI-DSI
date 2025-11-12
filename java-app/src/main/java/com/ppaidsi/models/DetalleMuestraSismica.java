package com.ppaidsi.models;

public class DetalleMuestraSismica {

    private final double valor;
    private final TipoDeDato tipoDeDato;

    public DetalleMuestraSismica(double valor, TipoDeDato tipoDeDato) {
        this.valor = valor;
        this.tipoDeDato = tipoDeDato;
    }

    public double getValor() {
        return valor;
    }

    public TipoDeDato getTipoDeDato() {
        return tipoDeDato;
    }
}


