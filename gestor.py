from modelos import *

class Gestor:
    def __init__(self, eventos):
        self.eventos = eventos  # lista de EventoSismico instances

    def buscarSismosParaRevision(self):
        # filtra eventos con estado pendienteRevision y actual
        pendientes = [e for e in self.eventos
                      if e.obtener_estado_actual() and e.obtener_estado_actual().nombre_estado == 'pendienteRevision']
        return pendientes
    
    def ordenarEventosPorFecha(self, eventos):
        return sorted(eventos, key=lambda e: e.fecha_hora_ocurrencia)
    
    def bloquearEventoSismico(self, evento):
        """
        Simplemente pasamos el Estado a la lista de cambios del evento.
        """
        estado_bloqueado = Estado('sismo', 'bloqueado')
        evento.agregar_cambio_estado(estado_bloqueado)

    def generarSismograma(self, evento):
        return "sismograma" # Aca se llamaria al caso de uso para generar el sismograma