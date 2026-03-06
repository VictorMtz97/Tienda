from reportlab.pdfgen import canvas
from datetime import datetime
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
import os

def generar_ticket(productos, total, pago, cambio):

    confirmar= messagebox.askyesno("Confirmar Venta", "Deseas generar el recibo??")

    if not confirmar:
        return
    
    carpeta_destino=r"C:\Users\USUARIO\Desktop\Programas\SistemaVentas\tickets"


    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    archivos = os.listdir(carpeta_destino)
    numero_ticket= len(archivos) + 1

    nombre_pdf = f"ticket_{numero_ticket}.pdf"
    ruta_final= os.path.join(carpeta_destino, nombre_pdf)

    pdf= canvas.Canvas(ruta_final, pagesize=A4)
    y=750

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y , f"Ticket Venta #{numero_ticket}")
    y-=30

    fecha= datetime.now().strftime("%d/%m/%Y %H:%M")
    pdf.drawString(50, y, f"Fecha: {fecha}")
    y-=20

    pdf.drawString(50, y, "Producto")
    pdf.drawString(200, y, "Precio")
    y -= 20

    for nombre, precio in productos:
        pdf.drawString(50, y, nombre)
        pdf.drawString(200, y, f"${precio}")
        y-=20

    y -= 20
    pdf.drawString(50, y, f"Total: ${total}")

    y -= 20
    pdf.drawString(50, y, f"Pago: ${pago}")

    y -= 20
    pdf.drawString(50, y, f"Cambio: ${cambio}")

    pdf.save()

    print(f"Archivo guardado en: {ruta_final}")