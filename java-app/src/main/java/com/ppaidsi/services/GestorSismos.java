package com.ppaidsi.services;

import com.ppaidsi.iterators.IAgregado;
import com.ppaidsi.iterators.IteradorEventoSismico;
import com.ppaidsi.iterators.iIterador;
import com.ppaidsi.models.Estado;
import com.ppaidsi.models.EventoSismico;
import com.ppaidsi.models.Sesion;
import com.ppaidsi.models.Usuario;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class GestorSismos implements IAgregado {

    private static final String ESTADO_PENDIENTE_REVISION = "pendienteRevision";

    private final List<EventoSismico> eventos;
    private final List<Sesion> sesiones;
    private final Estado estadoBloqueado;

    public GestorSismos(List<EventoSismico> eventos, List<Sesion> sesiones, Estado estadoBloqueado) {
        this.eventos = eventos;
        this.sesiones = sesiones;
        this.estadoBloqueado = estadoBloqueado;
    }

    @Override
    public iIterador crearIterador(Object[] elementos, Object[] filtro) {
        return new IteradorEventoSismico(elementos, filtro);
    }

    public List<EventoSismico> buscarSismosParaRevision() {
        var iterador = crearIterador(eventos.toArray(), new Object[]{ESTADO_PENDIENTE_REVISION});
        var resultado = new ArrayList<EventoSismico>();
        for (iterador.primero(); !iterador.haFinalizado(); iterador.siguiente()) {
            Object actual = iterador.elementoActual();
            if (actual instanceof EventoSismico evento) {
                resultado.add(evento);
            }
        }
        return resultado;
    }

    public List<EventoSismico> ordenarEventosPorFecha(List<EventoSismico> eventos) {
        return eventos.stream()
                .sorted(Comparator.comparing(EventoSismico::getFechaHoraOcurrencia))
                .toList();
    }

    public void bloquearEventoSismico(EventoSismico evento) {
        evento.agregarCambioEstado(estadoBloqueado);
    }

    public String generarSismograma(EventoSismico evento) {
        return "sismograma";
    }

    public boolean validarDatosSismo(EventoSismico evento) {
        return evento.getAlcance() >= 0
                && evento.getMagnitud() >= 0
                && evento.getOrigenGeneracion() != null
                && !evento.getOrigenGeneracion().isBlank();
    }

    public void actualizarEstadoEventoRechazado(EventoSismico evento) {
        if (!validarDatosSismo(evento)) {
            throw new IllegalArgumentException("Faltan datos: alcance, magnitud u origen");
        }
        evento.agregarCambioEstado(new Estado("sismo", "rechazado"));
    }

    public Optional<Usuario> buscarUsuarioActivo() {
        return sesiones.stream()
                .map(Sesion::buscarUsuario)
                .flatMap(Optional::stream)
                .findFirst();
    }

    public Optional<EventoSismico> buscarEventoPorId(int id) {
        return eventos.stream()
                .filter(evento -> evento.getId() == id)
                .findFirst();
    }
}

