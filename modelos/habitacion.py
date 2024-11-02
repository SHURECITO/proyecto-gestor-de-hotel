class Habitacion:
    def __init__(self, numero, tipo, capacidad, precio, descripcion):
        self.numero = numero
        self.tipo = tipo
        self.capacidad = capacidad
        self.precio = precio
        self.descripcion = descripcion
        self.disponibilidad = True

    def actualizar_disponibilidad(self, disponible):
        self.disponibilidad = disponible
