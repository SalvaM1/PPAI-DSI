from ..models.entidades import EventoSismico
from .. import db

class GestorSismos:
    def __init__(self):
        pass  # No necesitamos parámetros por ahora

    def obtener_pendientes(self):
        """
        Devuelve eventos con magnitud > 0 y sin procesar.
        """
        return EventoSismico.query.filter(
            EventoSismico.magnitud > 0
        ).all()

    def bloquear_evento(self, evento_id):
        evento = EventoSismico.query.get_or_404(evento_id)
        # Ejemplo: marcamos magnitud negativa como "bloqueado"
        evento.magnitud *= -1
        db.session.commit()
        return evento