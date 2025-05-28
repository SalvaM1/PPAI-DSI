from flask import Flask, render_template, request, abort
from datos import crear_eventos, crear_usuarios, crear_sesiones
from gestor import Gestor
from modelos import *


app = Flask(__name__)

# Cargamos los eventos y creamos el gestor
eventos = crear_eventos()
usuarios = crear_usuarios()
sesiones = crear_sesiones(usuarios)

# Si crear_eventos no asigna id, hazlo aquí:
for idx, e in enumerate(eventos, start=1):
    setattr(e, 'id', idx)

gestor = Gestor(eventos)
interfaz = Interfaz()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def mostrar_eventos():
    eventos_pendientes = gestor.solicitar_seleccion()
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

    # 4) Obtener usuario(s) de la sesión (ejemplo: la primera sesión)
    sesion = sesiones[0]  # O busca la sesión correspondiente
    usuarios_activos = gestor.buscar_usuario(sesion)
    #Intento de ver porque no anda
    #print("Usuarios activos:", [u.nombre for u in usuarios_activos]) 
    # 5) Renderizar la plantilla de detalle
    return render_template('evento_detalle.html', e=evento, usuario=usuarios_activos)

if __name__ == '__main__':
    app.run(debug=True)
