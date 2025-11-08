package com.ppaidsi.models;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

public class Sesion {

    private final List<Usuario> usuarios;
    private final int id;

    public Sesion(List<Usuario> usuarios, int id) {
        this.usuarios = new ArrayList<>(usuarios);
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public List<Usuario> getUsuarios() {
        return Collections.unmodifiableList(usuarios);
    }

    public Optional<Usuario> buscarUsuario() {
        return usuarios.stream()
                .filter(Usuario::esActual)
                .findFirst();
    }

    public boolean esUsuarioActual() {
        return usuarios.stream().anyMatch(Usuario::esActual);
    }
}
