package com.ppaidsi.iterators;

public interface iIterador {

    void primero();

    void siguiente();

    boolean haFinalizado();

    boolean comprobarFiltro(Object[] filtro);

    Object elementoActual();
}

