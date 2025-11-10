package com.ppaidsi.iterators;

import com.ppaidsi.models.EventoSismico;

import java.util.Arrays;

public class IteradorEventoSismico implements iIterador {

    private final EventoSismico[] lista;
    private final Object[] filtro;
    private int posicionActual;

    public IteradorEventoSismico(Object[] elementos, Object[] filtro) {
        Object[] elementosSeguros = elementos != null ? elementos : new Object[0];
        this.lista = Arrays.stream(elementosSeguros)
                .filter(EventoSismico.class::isInstance)
                .map(EventoSismico.class::cast)
                .toArray(EventoSismico[]::new);
        this.filtro = filtro != null ? filtro : new Object[0];
        this.posicionActual = 0;
        ajustarAPosicionValida();
    }

    @Override
    public void primero() {
        posicionActual = 0;
        ajustarAPosicionValida();
    }

    @Override
    public void siguiente() {
        if (!haFinalizado()) {
            posicionActual++;
            ajustarAPosicionValida();
        }
    }

    @Override
    public boolean haFinalizado() {
        return posicionActual >= lista.length;
    }

    @Override
    public boolean comprobarFiltro(Object[] filtro) {
        if (haFinalizado()) {
            return false;
        }
        var filtroActual = filtro != null ? filtro : new Object[0];
        var evento = lista[posicionActual];
        if (filtroActual.length == 0) {
            return true;
        }
        String estadoObjetivo = filtroActual.length > 0 && filtroActual[0] instanceof String
                ? (String) filtroActual[0]
                : null;
        String origenObjetivo = filtroActual.length > 1 && filtroActual[1] instanceof String
                ? (String) filtroActual[1]
                : null;
        boolean coincideEstado = estadoObjetivo == null
                || evento.obtenerEstadoActual()
                .map(estado -> estadoObjetivo.equalsIgnoreCase(estado.getNombreEstado()))
                .orElse(false);
        boolean coincideOrigen = origenObjetivo == null
                || (evento.getOrigenGeneracion() != null
                && origenObjetivo.equalsIgnoreCase(evento.getOrigenGeneracion()));
        return coincideEstado && coincideOrigen;
    }

    @Override
    public Object elementoActual() {
        if (haFinalizado()) {
            return null;
        }
        return lista[posicionActual];
    }

    private void ajustarAPosicionValida() {
        while (!haFinalizado() && !comprobarFiltro(filtro)) {
            posicionActual++;
        }
    }
}

