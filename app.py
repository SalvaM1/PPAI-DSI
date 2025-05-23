from flask import Flask, render_template
from datos import crear_eventos
from gestor import Gestor
from modelos import Interfaz

# Crear datos al iniciar la aplicación
eventos = crear_eventos()

# Inicializar Flask y componentes
app = Flask(__name__)
gestor = Gestor(eventos)
interfaz = Interfaz()

@app.route('/')
def index():
    # Muestra la página inicial con el botón
    return render_template('index.html')

@app.route('/eventos')
def mostrar_eventos():
    # Obtiene eventos pendientes y renderiza la tabla
    eventos_pendientes = gestor.solicitar_seleccion()
    return interfaz.mostrar_eventos(eventos_pendientes)

@app.route('/revisar/<int:evento_id>', methods=['POST'])
def revisar_evento(evento_id):
    # PRIMERO CAMBIAR EL ESTADO DEL EVENTO SELECCIONADO
    # Lógica para procesar la revisión (cambiar estado, etc.)
    # Aquí podrías usar gestor.agregar_cambio_estado(...) o similar
    return f"Evento {evento_id} seleccionado para revisión."

if __name__ == '__main__':
    app.run(debug=True)