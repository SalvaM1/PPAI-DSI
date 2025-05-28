from flask import Flask, render_template, request, abort, flash, redirect, url_for
from datos import crear_eventos, crear_usuarios, crear_sesiones
from gestor import Gestor
from modelos import *
import os


app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aquí')  

# Cargamos los eventos y creamos el gestor
eventos, estaciones, sismografos = crear_eventos()
usuarios = crear_usuarios()
sesiones = crear_sesiones(usuarios)

# Si crear_eventos no asigna id, hazlo aquí:
for idx, e in enumerate(eventos, start=1):
    setattr(e, 'id', idx)

gestor = Gestor(eventos)
interfaz = Interfaz()

@app.route('/')
def index():
    return interfaz.habilitarVentana()

@app.route('/eventos')
def mostrar_eventos():
    eventos_pendientes = gestor.buscarSismosParaRevision()
    eventos_ordenados = gestor.ordenarEventosPorFecha(eventos_pendientes)
    return interfaz.mostrar_eventos(eventos_pendientes)

@app.route('/revisar', methods=['GET'])
def revisar_evento():
    # 1) Leer id desde la query string
    id_str = request.args.get('id')
    if not id_str:
        abort(400, "Falta el parámetro 'id'")
    try:
        evento_id = int(id_str)
    except ValueError: 
        abort(400, "Parámetro 'id' inválido")

    # 2) Buscar el evento
    evento = next((e for e in gestor.eventos if getattr(e, 'id', None) == evento_id), None)
    if not evento:
        abort(404, f"No existe evento con id {evento_id}")
    

    # 3) Cambiar estado del evento a bloqueado creando un nuevo cambio estado para el evento que tiene el id de la uri, usando un metodo en la clase gestor
    gestor.bloquearEventoSismico(evento)   
    for serie in evento.series_temporales:
        serie.estacion = serie.esMiSismografo(sismografos)

    sismograma= gestor.generarSismograma(evento)

    # 4) Obtener usuario(s) de la sesión (ejemplo: la primera sesión)
    sesion = sesiones[0]  # O busca la sesión correspondiente
    usuarios_activos = gestor.buscar_usuario(sesion)


    return interfaz.mostrarEventoSeleccionado(evento, usuarios_activos)


@app.route('/rechazar', methods=['POST'], endpoint='rechazar')
def rechazar_evento():
    evento_id = int(request.form['id'])

    # Obtenés los datos directamente desde el gestor
    alcance, magnitud, origen = gestor.buscarDatosSismo(evento_id)

    # 2) Buscar evento
    evento = next((e for e in gestor.eventos if e.id == evento_id), None)
    if not evento:
        abort(404, f"No existe evento con id {evento_id}")

    # 3) Validación de datos recibidos
    if not (alcance and magnitud and origen):
        flash("Faltan datos de alcance, magnitud u origen.", "danger")
        return redirect(url_for('revisar_evento', id=evento_id))

    evento.alcance   = float(alcance)
    evento.magnitud  = float(magnitud)
    evento.origen_generacion = origen

    # 4) Rechazar con tu método
    try:
        gestor.actualizarEstadoEventoRechazado(evento)
        flash("Evento rechazado ✅", "success")
    except ValueError as e:
        flash(str(e), "danger")
        return redirect(url_for('revisar_evento', id=evento_id))

    # 5) Volver al listado
    return redirect(url_for('mostrar_eventos'))


if __name__ == '__main__':
    app.run(debug=True)
