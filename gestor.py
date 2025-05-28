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
        estado_bloqueado = Estado('sismo', 'bloqueado')
        evento.agregar_cambio_estado(estado_bloqueado)

    def generarSismograma(self, evento):
        return "sismograma" # Aca se llamaria al caso de uso para generar el sismograma

    def validarDatosSismo(self, evento):
        return all([
            evento.alcance   is not None,
            evento.magnitud  is not None,
            bool(evento.origen_generacion and evento.origen_generacion.strip())
        ])

    def actualizarEstadoEventoRechazado(self, evento):
        if not self.validarDatosSismo(evento):
            raise ValueError("Faltan datos: alcance, magnitud u origen")
        evento.agregar_cambio_estado(Estado('sismo', 'rechazado'))
        print(f"[Gestor] Evento {evento.id} ahora en estado: {evento.obtener_estado_actual().nombre_estado}")

    
    def buscar_usuario(self, sesion):
        return sesion.buscarUsuario()
    
    def buscarDatosSismo(self, evento_id):
        evento = next((e for e in self.eventos if getattr(e, 'id', None) == evento_id), None)
        if evento:
            return evento.alcance, evento.magnitud, evento.origen_generacion
        else:
            return None, None, None
