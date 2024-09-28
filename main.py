from sistema_registro import SistemaRegistro

def main():
    sistema = SistemaRegistro()
    
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Cambiar contraseña")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo electrónico: ")
            contrasena = input("Ingrese su contraseña: ")
            sistema.enviar_registro(nombre, correo, contrasena)
        
        elif opcion == "2":
            correo = input("Ingrese su correo electrónico: ")
            contrasena = input("Ingrese su contraseña: ")
            sistema.enviar_formulario_inicio_sesion(correo, contrasena)
        
        elif opcion == "3":
            if sistema.usuario_autenticado is None:
                print("Debes iniciar sesión para cambiar tu contraseña.")
                continue
            correo = sistema.usuario_autenticado.correo
            contrasena_actual = input("Ingrese su contraseña actual: ")
            nueva_contrasena = input("Ingrese su nueva contraseña: ")
            sistema.enviar_formulario_cambio_contrasena(correo, contrasena_actual, nueva_contrasena)
        
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()