package com.ppaidsi.services;

import com.ppaidsi.data.DataFactory;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class GestorSismosTest {

    private GestorSismos gestorSismos;

    @BeforeEach
    void setUp() {
        var datos = DataFactory.crearDatos();
        gestorSismos = new GestorSismos(datos.eventos(), datos.sesiones(), datos.estadoBloqueado());
    }

    @Test
    void buscarSismosParaRevision_devuelveSoloPendientes() {
        var pendientes = gestorSismos.buscarSismosParaRevision();
        assertThat(pendientes)
                .isNotEmpty()
                .allMatch(evento -> evento.obtenerEstadoActual()
                        .map(estado -> "pendienteRevision".equalsIgnoreCase(estado.getNombreEstado()))
                        .orElse(false));
    }

    @Test
    void bloquearEventoSismico_agregaEstadoBloqueado() {
        var evento = gestorSismos.buscarSismosParaRevision().getFirst();
        gestorSismos.bloquearEventoSismico(evento);
        assertThat(evento.obtenerEstadoActual())
                .isPresent()
                .get()
                .extracting(estado -> estado.getNombreEstado())
                .isEqualTo("bloqueado");
    }
}

