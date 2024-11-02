class Usuario:
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self._contrasena = contrasena

    def verificar_contrasena(self, contrasena):
        return self._contrasena == contrasena

    def cambiar_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena
