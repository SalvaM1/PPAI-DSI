package com.ppaidsi.controllers;

import com.ppaidsi.models.EventoSismico;
import com.ppaidsi.services.GestorSismos;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.List;

@Controller
public class EventosController {

    private final GestorSismos gestorSismos;

    public EventosController(GestorSismos gestorSismos) {
        this.gestorSismos = gestorSismos;
    }

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/eventos")
    public String listarEventos(Model model) {
        List<EventoSismico> pendientes = gestorSismos.buscarSismosParaRevision();
        model.addAttribute("eventos", gestorSismos.ordenarEventosPorFecha(pendientes));
        return "eventos";
    }

    @GetMapping("/eventos/revisar")
    public String revisarEvento(@RequestParam("id") int id, Model model, RedirectAttributes redirectAttributes) {
        return gestorSismos.buscarEventoPorId(id)
                .map(evento -> {
                    gestorSismos.bloquearEventoSismico(evento);
                    model.addAttribute("evento", evento);
                    model.addAttribute("usuario", gestorSismos.buscarUsuarioActivo().orElse(null));
                    model.addAttribute("sismograma", gestorSismos.generarSismograma(evento));
                    return "evento_detalle";
                })
                .orElseGet(() -> {
                    redirectAttributes.addFlashAttribute("error", "No existe evento con id " + id);
                    return "redirect:/eventos";
                });
    }

    @PostMapping("/eventos/rechazar")
    public String rechazarEvento(
            @RequestParam("id") int id,
            @RequestParam("alcance") double alcance,
            @RequestParam("magnitud") double magnitud,
            @RequestParam("origen") String origen,
            RedirectAttributes redirectAttributes
    ) {
        return gestorSismos.buscarEventoPorId(id)
                .map(evento -> {
                    evento.setAlcance(alcance);
                    evento.setMagnitud(magnitud);
                    evento.setOrigenGeneracion(origen);
                    try {
                        gestorSismos.actualizarEstadoEventoRechazado(evento);
                        redirectAttributes.addFlashAttribute("success", "Evento rechazado correctamente");
                    } catch (IllegalArgumentException ex) {
                        redirectAttributes.addFlashAttribute("error", ex.getMessage());
                    }
                    return "redirect:/eventos";
                })
                .orElseGet(() -> {
                    redirectAttributes.addFlashAttribute("error", "No existe evento con id " + id);
                    return "redirect:/eventos";
                });
    }
}

