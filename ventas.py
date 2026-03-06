import tkinter as tk
from  tkinter import ttk
from productos import TablaProductos
from tkinter import messagebox
from recibo import generar_ticket
import csv



class Ventas(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg="#355872")
        self.controlador = controlador


        tk.Label(self, text="Este es el cajero, puedes observar los productos y realizar una pago con ticket.", font=("Segoe UI", 16)).pack(pady=10)
        container_botones= tk.Frame(self, bg="#355872")
        container_botones.pack(fill="x", padx=30, pady=10)

        tk.Button(container_botones, text="Añadir", command=self.añadir_carrito, width=12, font=("Segoe UI", 12)).pack(side="left")
        tk.Button(container_botones, text="Limpiar", command=self.limpiar_campos, width=12, font=("Segoe UI", 12)).pack(side="right")

        frame_tablas= tk.Frame(self)
        frame_tablas.pack(fill="y")

        #Tabla de productos
        self.tabla_productos = TablaProductos(frame_tablas)
        self.tabla_productos.pack(side="left", fill="y", pady=10)
        #Tabla de productos
        

        #Tabla Carrito
        columnas = ("id","nombre","precio")
        self.tabla_carrito = ttk.Treeview(frame_tablas, columns = columnas, show= "headings")
        self.tabla_carrito.heading("id", text="ID")
        self.tabla_carrito.heading("nombre", text = "Nombre")
        self.tabla_carrito.heading("precio", text = "Precio")
        self.tabla_carrito.column("id", width=50, anchor="center")
        self.tabla_carrito.column("nombre", width=150, anchor="center")
        self.tabla_carrito.column("precio", width=100, anchor="center")
        self.tabla_carrito.pack(side="left", fill="y", padx=10)
        #Tabla Carrito

        frame_caja= tk.Frame(self, bg="#355872")
        frame_caja.pack(side="right", fil="y", pady=10)

        tk.Label(frame_caja, text="Caja", font=("Arial", 12, "bold")).pack(pady=10)
        self.label_total= tk.Label(frame_caja, text="", font=("Arial", 12, "bold"))
        self.label_total.pack(pady=10)

        tk.Label(frame_caja, text="Ingreso:", font=("Arial", 12, "bold")).pack(pady=10)
        self.pago = tk.Entry(frame_caja, state="disabled")
        self.pago.pack(pady=10)
        self.label_cambio= tk.Label(frame_caja, text="", font=("Arial", 12, "bold"))
        self.label_cambio.pack(pady=10)


        tk.Button(frame_caja, text="Ingresar", command=self.cambio_carrito,font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(frame_caja, text="Pagado", command=self.imprimir_ticket, font=("Arial", 12, "bold")).pack(pady=10)


    def añadir_carrito(self):
        seleccion = self.tabla_productos.tree.selection()
        if not seleccion:
             return messagebox.showwarning("Advertencia","no se ha seleccionado ninguno para eliminar")

        item = seleccion[0]
        valores = self.tabla_productos.tree.item(item)["values"]

        id = valores[0]
        nombre = valores[1]
        precio = valores[2]
        stock = int(valores[3])

        #Valido el stock
        if stock <= 0:
            messagebox.showerror("Sin stock", "Este producto no tiene stock")
            return

        self.tabla_carrito.insert("", tk.END, values= (id, nombre,precio))

        self.suma_carrito()
        self.pago.config(state="normal")
        

    def actualizar_csv(self,id_producto,nuevo_stock):
        archivo = "productos.csv"
        filas = []

        with open(archivo, "r", newline="") as f:
            reader = csv.reader(f)

            for fila in reader:
                if fila[0] == str(id_producto):
                    fila[3] = str(nuevo_stock)

                filas.append(fila)

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas)

    def suma_carrito(self):

        total=0
        for item in self.tabla_carrito.get_children():
            valores =  self.tabla_carrito.item(item)["values"]
            subtotal= float(valores[2])
            total += subtotal
        self.label_total.config(text=f"Total a pagar: ${total}")

    def cambio_carrito(self):

        if not self.tabla_carrito.get_children():
            return messagebox.showwarning("Carrito vacío", "No hay productos en el carrito")

        try:
            pago = float(self.pago.get())
        except ValueError:
            return messagebox.showerror("Error", "Ingresa una cantidad válida")

        if pago< 0:
            return messagebox.showwarning("Error", "El pago no puede ser negativo")

        total_texto = self.label_total.cget("text")
        total= float(total_texto.replace("Total a pagar: $", ""))
        cambio = pago - total
        self.label_cambio.config(text=f"Cambio: {cambio}")

    def imprimir_ticket(self):

        productos = []
        total = 0

        for item in self.tabla_carrito.get_children():

            valores = self.tabla_carrito.item(item)["values"]

            id_producto = valores[0]
            nombre = valores[1]
            precio = float(valores[2])

            productos.append((nombre, precio))
            total += precio

            # descontar stock
            self.descontar_stock(id_producto)

        pago = float(self.pago.get())
        cambio = pago - total

        generar_ticket(productos, total, pago, cambio)
        self.limpiar_campos()

    def descontar_stock(self, id_producto):
        
        archivo = "productos.csv"
        filas = []

        with open(archivo,"r",newline="") as f:
            reader = csv.reader(f)

            for fila in reader:

                if fila[0] == str(id_producto):

                    stock = int(fila[3])
                    stock -= 1
                    fila[3] = str(stock)

                filas.append(fila)

        with open(archivo,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas)


    def limpiar_campos(self):
        if not self.tabla_carrito.get_children():
            messagebox.showinfo("Carrito Vacio","No hay productos en el carrito")
            return
        confirmar= messagebox.askyesno("Confirmar", "Estas seguro que quieres vaciar el carrito?")
        if not confirmar:
            return
        self.tabla_carrito.delete(*self.tabla_carrito.get_children())
        self.label_cambio.config(text="")
        self.pago.delete(0, tk.END)
        messagebox.showinfo("Listo", "El carrito se limpio.")
        self.suma_carrito()





