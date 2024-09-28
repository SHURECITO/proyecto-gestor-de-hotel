class Usuario:
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self._contrasena = contrasena #Este _ sirve para que sea privado en esta clase (un poquito mas de seguridad ;) )

    def verificar_contrasena(self, contrasena):
        return self._contrasena == contrasena

    def cambiar_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena