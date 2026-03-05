from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import messagebox

def generar_ticket(productos, total, pago, cambio):

    confirmar= messagebox.askyesno("Confirmar Venta", "Deseas generar el recibo??")

    if not confirmar:
        return

    pdf= canvas.Canvas("ticket_ventas.pdf")

    y=750

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y , "Ticket Venta")
    y-=30

    fecha= datetime.now().strftime("%d/%m/%Y %H:%M")
    pdf.drawString(50, y, f"Fecha: {fecha}")
    y-=20

    pdf.drawString(50, y, "Producto")
    pdf.drawString(200, y, "Precio")
    y -= 20

    for nombre, precio in productos:
        pdf.drawString(50, y, nombre)
        pdf.drawString(2000, y, f"${precio}")
        y-=20

    y -= 20
    pdf.drawString(50, y, f"Total: ${total}")

    y -= 20
    pdf.drawString(50, y, f"Pago: ${pago}")

    y -= 20
    pdf.drawString(50, y, f"Cambio: ${cambio}")

    pdf.save()

