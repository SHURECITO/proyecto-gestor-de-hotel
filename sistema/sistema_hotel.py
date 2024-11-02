from modelos.habitacion import Habitacion
from modelos.reserva import Reserva

class SistemaHotel:
    def __init__(self):
        self.habitaciones = {str(numero): Habitacion(numero, "Tipo", 2, 100.0, f"Descripción de la habitación {numero}") for numero in range(100, 116)}
        self.reservas = []

    def registrar_habitacion(self, numero, tipo, capacidad, precio, descripcion):
        if numero in self.habitaciones:
            print("Error: La habitación ya está registrada.")
            return False
        nueva_habitacion = Habitacion(numero, tipo, capacidad, precio, descripcion)
        self.habitaciones[numero] = nueva_habitacion
        print(f"Habitación {numero} registrada con éxito.")
        return True

    def buscar_habitaciones_disponibles(self, fecha_inicio, fecha_fin):
        return [habitacion for habitacion in self.habitaciones.values() if habitacion.disponibilidad]

    def realizar_reserva(self, id_usuario, numero_habitacion, fecha_inicio, fecha_fin):
        if numero_habitacion not in self.habitaciones or not self.habitaciones[numero_habitacion].disponibilidad:
            print("Error: La habitación no está disponible.")
            return False
        nueva_reserva = Reserva(id_usuario, numero_habitacion, fecha_inicio, fecha_fin)
        self.reservas.append(nueva_reserva)
        self.habitaciones[numero_habitacion].actualizar_disponibilidad(False)
        print(f"Reserva realizada exitosamente para la habitación {numero_habitacion}.")
        return True

    def cancelar_reserva(self, id_reserva):
        reserva = next((r for r in self.reservas if r.id == id_reserva and r.estado == "Activa"), None)
        if reserva:
            reserva.cancelar_reserva()
            self.habitaciones[reserva.id_habitacion].actualizar_disponibilidad(True)
            print(f"Reserva {id_reserva} cancelada exitosamente.")
            return True
        print(f"Error: Reserva {id_reserva} no encontrada o ya está cancelada.")
        return False

    def modificar_reserva(self, id_reserva, nueva_fecha_inicio, nueva_fecha_fin):
        reserva = next((r for r in self.reservas if r.id == id_reserva and r.estado == "Activa"), None)
        if reserva:
            if self.habitaciones[reserva.id_habitacion].disponibilidad:
                reserva.fecha_inicio = nueva_fecha_inicio
                reserva.fecha_fin = nueva_fecha_fin
                print(f"Reserva {id_reserva} actualizada exitosamente.")
                return True
            print("Error: La habitación no está disponible para las nuevas fechas.")
            return False
        print(f"Error: Reserva {id_reserva} no encontrada o ya está cancelada.")
        return False

    def __init__(self):
        self.habitaciones = {}
        self.reservas = []

    def obtener_reservas_usuario(self, correo_usuario):
        return [reserva for reserva in self.reservas if reserva.id_usuario == correo_usuario]

    def modificar_reserva(self, reserva, nueva_fecha_inicio, nueva_fecha_fin):
        reserva.fecha_inicio = nueva_fecha_inicio
        reserva.fecha_fin = nueva_fecha_fin

    def cancelar_reserva(self, reserva):
        reserva.estado = "Cancelada"
