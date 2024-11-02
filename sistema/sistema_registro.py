from modelos.usuario import Usuario

class SistemaRegistro:
    def __init__(self):
        self.usuarios = {}
        self.usuario_autenticado = None

    def enviar_registro(self, nombre, correo, contrasena):
        if self.validar_datos_registro(correo):
            print("Error: El correo ya está registrado.")
            return False
        self.crear_usuario(nombre, correo, contrasena)
        print(f"Usuario {nombre} registrado con éxito.")
        return True

    def validar_datos_registro(self, correo):
        return correo in self.usuarios

    def crear_usuario(self, nombre, correo, contrasena):
        nuevo_usuario = Usuario(nombre, correo, contrasena)
        self.usuarios[correo] = nuevo_usuario

    def enviar_formulario_cambio_contrasena(self, correo, contrasena_actual, nueva_contrasena):
        if self.usuario_autenticado is None or self.usuario_autenticado.correo != correo:
            print("Error: Debes iniciar sesión antes de cambiar la contraseña.")
            return False
        if self.verificar_contrasena_actual(correo, contrasena_actual):
            self.actualizar_contrasena_usuario(correo, nueva_contrasena)
            self.confirmar_cambio_contrasena()
            return True
        else:
            print("Error: La contraseña actual es incorrecta.")
            return False

    def verificar_contrasena_actual(self, correo, contrasena_actual):
        return self.usuarios[correo].verificar_contrasena(contrasena_actual)

    def actualizar_contrasena_usuario(self, correo, nueva_contrasena):
        self.usuarios[correo].cambiar_contrasena(nueva_contrasena)

    def confirmar_cambio_contrasena(self):
        print("Contraseña actualizada con éxito.")

    def enviar_formulario_inicio_sesion(self, correo, contrasena):
        if correo not in self.usuarios:
            print("Error: El usuario no existe.")
            return False
        validacion = self.validar_credenciales(correo, contrasena)
        return self.otorgar_acceso_usuario(validacion, correo)

    def validar_credenciales(self, correo, contrasena):
        return self.usuarios[correo].verificar_contrasena(contrasena)

    def otorgar_acceso_usuario(self, validacion, correo):
        if validacion:
            self.usuario_autenticado = self.usuarios[correo]
            print("Datos correctos. Bienvenido!")
            return self.usuario_autenticado
        else:
            print("Error: Credenciales incorrectas.")
            return False
