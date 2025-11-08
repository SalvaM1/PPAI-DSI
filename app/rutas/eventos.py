from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..servicios.gestor import GestorSismos

# Crear blueprint
eventos_bp = Blueprint('eventos', __name__, template_folder='../templates')

# Instancia del gestor
gestor = GestorSismos()

@eventos_bp.route('/')
def listar():
    eventos = gestor.obtener_pendientes()
    return render_template('eventos.html', eventos=eventos)

@eventos_bp.route('/bloquear', methods=['POST'])
def bloquear():
    id = request.form.get('id')
    try:
        evento = gestor.bloquear_evento(int(id))
        flash(f"Evento {evento.id} bloqueado.")
    except Exception as e:
        flash(str(e), 'error')
    return redirect(url_for('eventos.listar'))