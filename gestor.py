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

    def validarDatosSismo(self, evento):
        return all([
            evento.alcance   is not None,
            evento.magnitud  is not None,
            bool(evento.origen_generacion and evento.origen_generacion.strip())
        ])

    def rechazarEventoSismico(self, evento):
        if not self.validarDatosSismo(evento):
            raise ValueError("Faltan datos: alcance, magnitud u origen")
        evento.agregar_cambio_estado(Estado('sismo', 'rechazado'))
        print(f"[Gestor] Evento {evento.id} ahora en estado: {evento.obtener_estado_actual().nombre_estado}")
