from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_reporte_reservas(reservas, fecha_inicio, fecha_fin, filename="reporte_reservas.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"Reporte de Reservas desde {fecha_inicio} hasta {fecha_fin}")
    
    y_position = 700
    for reserva in reservas:
        c.drawString(100, y_position, f"ID Reserva: {reserva.id_usuario}, Habitación: {reserva.id_habitacion}, Estado: {reserva.estado}")
        y_position -= 20

    c.save()
    print(f"Reporte guardado como {filename}")