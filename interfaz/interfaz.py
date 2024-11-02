import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar
from sistema.sistema_registro import SistemaRegistro
from sistema.sistema_hotel import SistemaHotel
from utils.generador_pdf import generar_reporte_reservas
import re
from tkinter import font as tkFont
import datetime
reserva = 0

class Interfaz:
    def __init__(self, root):
        self.sistema_registro = SistemaRegistro()
        self.sistema_hotel = SistemaHotel()

        # Inicializar habitaciones de 100 a 115 como disponibles
        for numero in range(100, 116):
            self.sistema_hotel.registrar_habitacion(str(numero), "Estándar", 2, 100, "Descripción")

        self.fondo_color = "#f0f0f5"
        self.texto_color = "#4f4f4f"
        self.boton_color = "#66b2b2"
        self.boton_hover = "#4d99a6"

        root.title("Sistema de Gestión de Hotel")
        root.geometry("500x600")
        root.config(bg=self.fondo_color)

        self.fuente_principal = tkFont.Font(family="Montserrat", size=12)
        self.fuente_titulo = tkFont.Font(family="Montserrat", size=16, weight="bold")
        self.fuente_botones = tkFont.Font(family="Montserrat", size=10)

        self.style = ttk.Style()
        self.style.configure("Rounded.TButton", font=self.fuente_botones, background=self.boton_color, foreground="black", borderwidth=1, focuscolor="none")
        self.style.map("Rounded.TButton", background=[("active", self.boton_hover)])

        self.frame_inicial(root)

    def frame_inicial(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Bienvenido al Sistema de Gestión de Hotel", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=30)
        ttk.Button(root, text="Iniciar Sesión", style="Rounded.TButton", command=lambda: self.frame_login(root)).pack(pady=10)
        ttk.Button(root, text="Registrarse", style="Rounded.TButton", command=lambda: self.frame_registro(root)).pack(pady=10)

    def frame_login(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Iniciar Sesión", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)

        correo = ttk.Entry(root, font=self.fuente_principal, width=30)
        contrasena = ttk.Entry(root, font=self.fuente_principal, show="*", width=30)

        tk.Label(root, text="Correo:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        correo.pack()
        tk.Label(root, text="Contraseña:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        contrasena.pack()

        def login():
            if self.sistema_registro.enviar_formulario_inicio_sesion(correo.get(), contrasena.get()):
                messagebox.showinfo("Éxito", "Sesión iniciada.")
                self.frame_principal(root)
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")

        ttk.Button(root, text="Iniciar Sesión", style="Rounded.TButton", command=login).pack(pady=15)
        ttk.Button(root, text="Volver", style="Rounded.TButton", command=lambda: self.frame_inicial(root)).pack()

    def frame_registro(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Registrar Usuario", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)

        nombre = ttk.Entry(root, font=self.fuente_principal, width=30)
        correo = ttk.Entry(root, font=self.fuente_principal, width=30)
        contrasena = ttk.Entry(root, font=self.fuente_principal, show="*", width=30)

        tk.Label(root, text="Nombre:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        nombre.pack()
        tk.Label(root, text="Correo:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        correo.pack()
        tk.Label(root, text="Contraseña:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        contrasena.pack()

        def registrar():
            if not re.match(r"[^@]+@[^@]+\.[^@]+", correo.get()):
                messagebox.showerror("Error", "Por favor ingresa un correo válido.")
                return

            if self.sistema_registro.enviar_registro(nombre.get(), correo.get(), contrasena.get()):
                messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
                self.frame_inicial(root)
            else:
                messagebox.showerror("Error", "El correo ya está registrado.")

        ttk.Button(root, text="Registrar", style="Rounded.TButton", command=registrar).pack(pady=15)
        ttk.Button(root, text="Volver", style="Rounded.TButton", command=lambda: self.frame_inicial(root)).pack()

    def frame_principal(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Menú Principal", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)
        ttk.Button(root, text="Buscar Habitaciones", style="Rounded.TButton", command=lambda: self.frame_buscar_habitaciones(root)).pack(pady=10)
        ttk.Button(root, text="Realizar Reserva", style="Rounded.TButton", command=lambda: self.frame_realizar_reserva(root)).pack(pady=10)
        ttk.Button(root, text="Generar Reporte", style="Rounded.TButton", command=self.generar_reporte).pack(pady=10)
        ttk.Button(root, text="Mis Reservas", style="Rounded.TButton", command=lambda: self.frame_mis_reservas(root)).pack(pady=10)
        ttk.Button(root, text="Perfil", style="Rounded.TButton", command=lambda: self.frame_perfil(root)).pack(pady=20)

    def generar_reporte(self):
        try:
            fecha_inicio = simpledialog.askstring("Fecha de inicio", "Ingrese la fecha de inicio (YYYY-MM-DD):")
            fecha_fin = simpledialog.askstring("Fecha de fin", "Ingrese la fecha de fin (YYYY-MM-DD):")

            fecha_inicio_obj = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin_obj = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")

            if fecha_inicio_obj > fecha_fin_obj:
                messagebox.showerror("Error", "La fecha de inicio no puede ser posterior a la fecha de fin.")
                return

            generar_reporte_reservas(reserva, fecha_inicio, fecha_fin)
            messagebox.showinfo("Éxito", "Reporte generado exitosamente.")
        
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Por favor, use YYYY-MM-DD.")

    def frame_buscar_habitaciones(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Habitaciones Disponibles", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)

        frame_habitaciones = tk.Frame(root, bg=self.fondo_color)
        frame_habitaciones.pack()

        for i, habitacion in enumerate(self.sistema_hotel.habitaciones.values()):
            color = "green" if habitacion.disponibilidad else "red"
            estado = "Disponible" if habitacion.disponibilidad else "Reservado"
            boton = tk.Button(frame_habitaciones, text=f"{habitacion.numero}", font=self.fuente_principal, bg=color, fg="white", width=5, height=2)
            boton.grid(row=i//5, column=i%5, padx=5, pady=5)

        ttk.Button(root, text="Volver al Menú Principal", style="Rounded.TButton", command=lambda: self.frame_principal(root)).pack(pady=20)

    def frame_realizar_reserva(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        root.geometry("500x600")
        tk.Label(root, text="Realizar Reserva", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)

        numero_habitacion = ttk.Entry(root, font=self.fuente_principal, width=30)
        fecha_inicio = Calendar(root, selectmode='day')
        fecha_fin = Calendar(root, selectmode='day')

        tk.Label(root, text="Número de Habitación:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        numero_habitacion.pack()
        tk.Label(root, text="Fecha de Inicio:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        fecha_inicio.pack(pady=10)
        tk.Label(root, text="Fecha de Fin:", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_principal).pack()
        fecha_fin.pack(pady=10)

        def reservar():
            id_usuario = self.sistema_registro.usuario_autenticado.correo
            if self.sistema_hotel.realizar_reserva(id_usuario, numero_habitacion.get(), fecha_inicio.get_date(), fecha_fin.get_date()):
                messagebox.showinfo("Éxito", "Reserva realizada con éxito.")
                self.frame_principal(root)
                reserva += 1
            else:
                messagebox.showerror("Error", "No se pudo realizar la reserva.")

        ttk.Button(root, text="Reservar", style="Rounded.TButton", command=reservar).pack(pady=10)
        ttk.Button(root, text="Volver al Menú Principal", style="Rounded.TButton", command=lambda: self.frame_principal(root)).pack()

    def frame_mis_reservas(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Mis Reservas", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)
        
        for reserva in self.sistema_hotel.obtener_reservas_usuario(self.sistema_registro.usuario_autenticado.correo):
            frame = tk.Frame(root, bg=self.fondo_color, padx=10, pady=5)
            frame.pack(pady=5, fill="x")
            
            label = tk.Label(frame, text=f"Reserva {reserva.id_habitacion} - {reserva.fecha_inicio} a {reserva.fecha_fin}", font=self.fuente_principal)
            label.pack(side="left")

            ttk.Button(frame, text="Modificar", style="Rounded.TButton", command=lambda r=reserva: self.modificar_reserva(r, root)).pack(side="left", padx=5)
            ttk.Button(frame, text="Eliminar", style="Rounded.TButton", command=lambda r=reserva: self.eliminar_reserva(r, root)).pack(side="left", padx=5)

        ttk.Button(root, text="Volver al Menú Principal", style="Rounded.TButton", command=lambda: self.frame_principal(root)).pack(pady=20)

    def modificar_reserva(self, reserva, root):
        nueva_fecha_inicio = simpledialog.askstring("Modificar Reserva", "Nueva Fecha de Inicio (YYYY-MM-DD):")
        nueva_fecha_fin = simpledialog.askstring("Modificar Reserva", "Nueva Fecha de Fin (YYYY-MM-DD):")
        if nueva_fecha_inicio and nueva_fecha_fin:
            self.sistema_hotel.modificar_reserva(reserva, nueva_fecha_inicio, nueva_fecha_fin)
            messagebox.showinfo("Éxito", "Reserva modificada con éxito.")
            self.frame_mis_reservas(root)

    def eliminar_reserva(self, reserva, root):
        self.sistema_hotel.cancelar_reserva(reserva)
        messagebox.showinfo("Éxito", "Reserva eliminada con éxito.")
        self.frame_mis_reservas(root)

    def frame_perfil(self, root):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="Perfil de Usuario", bg=self.fondo_color, fg=self.texto_color, font=self.fuente_titulo).pack(pady=20)

        def cambiar_contrasena():
            nueva_contrasena = simpledialog.askstring("Cambiar Contraseña", "Ingrese la nueva contraseña:", show="*")
            if nueva_contrasena:
                self.sistema_registro.usuario_autenticado.cambiar_contrasena(nueva_contrasena)
                messagebox.showinfo("Éxito", "Contraseña actualizada con éxito.")

        ttk.Button(root, text="Cambiar Contraseña", style="Rounded.TButton", command=cambiar_contrasena).pack(pady=10)
        ttk.Button(root, text="Cerrar Sesión", style="Rounded.TButton", command=lambda: self.frame_inicial(root)).pack(pady=10)
        ttk.Button(root, text="Volver", style="Rounded.TButton", command=lambda: self.frame_principal(root)).pack(pady=10)
