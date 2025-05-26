from modelos import *

class Gestor:
    def __init__(self, eventos):
        self.eventos = eventos  # lista de EventoSismico instances

    def solicitar_seleccion(self):
        # filtra eventos con estado pendienteRevision y actual
        pendientes = [e for e in self.eventos
                      if e.obtener_estado_actual() and e.obtener_estado_actual().nombre_estado == 'pendienteRevision']
        # ordena por fecha de ocurrencia
        pendientes.sort(key=lambda e: e.fecha_hora_ocurrencia)
        return pendientes

    def bloquearEventoSismico(self, evento):
        """
        Simplemente pasamos el Estado a la lista de cambios del evento.
        """
        estado_bloqueado = Estado('sismo', 'bloqueado')
        evento.agregar_cambio_estado(estado_bloqueado)