package com.ppaidsi;

import com.ppaidsi.data.DataFactory;
import com.ppaidsi.models.EventoSismico;
import com.ppaidsi.models.Sesion;
import com.ppaidsi.services.GestorSismos;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

@Configuration
public class AppConfig {

    @Bean
    public DataFactory.DatosIniciales datosIniciales() {
        return DataFactory.crearDatos();
    }

    @Bean
    public GestorSismos gestorSismos(DataFactory.DatosIniciales datosIniciales) {
        return new GestorSismos(
                datosIniciales.eventos(),
                datosIniciales.sesiones(),
                datosIniciales.estadoBloqueado()
        );
    }

    @Bean
    public List<EventoSismico> eventos(DataFactory.DatosIniciales datosIniciales) {
        return datosIniciales.eventos();
    }

    @Bean
    public List<Sesion> sesiones(DataFactory.DatosIniciales datosIniciales) {
        return datosIniciales.sesiones();
    }
}

