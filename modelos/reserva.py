class Reserva:
    def __init__(self, id_usuario, id_habitacion, fecha_inicio, fecha_fin):
        self.id_usuario = id_usuario
        self.id_habitacion = id_habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "Activa"

    def cancelar_reserva(self):
        self.estado = "Cancelada"
