import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import csv


class Productos(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador

        tk.Label(self, text="Aqui van los productos").pack(pady=10)

        tk.Label(self, text = "Nombre del producto").pack(pady=10)
        self.producto_entry = tk.Entry(self)
        self.producto_entry.pack(pady=5)

        tk.Label(self, text = "Precio del producto").pack(pady=10)
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)

        tk.Label(self, text = "Cantidad en stock del producto").pack(pady=10)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.pack(pady=5)

        tk.Button(self, text="Añadir", command=self.agregar_productos).pack(pady=10)
        tk.Button(self, text="Eliminar", command=self.eliminar_producto).pack(pady=10)

        self.tabla = TablaProductos(self)
        self.tabla.pack(fill="both", expand=True, pady=20)
        self.tree = self.tabla.tree
        

    def agregar_productos(self):
        
        nombre = self.producto_entry.get()
        precio = self.precio_entry.get()
        stock =  self.stock_entry.get()

        if not nombre or not precio or not stock:
           return messagebox.showwarning("Advertencia", "Te falto un dato revisa de nuevo")

        archivo="productos.csv"

        if os.path.exists(archivo):
            with open(archivo, "r", newline="") as f:
                reader= list(csv.reader(f))
                nuevo_id = len(reader)
        else:
            nuevo_id = 1

        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nuevo_id, nombre, precio, stock])

        self.tree.insert("", tk.END, values=(nuevo_id, nombre, precio, stock))

        self.limpiar_campos()


    def eliminar_producto(self):
        seleccion = self.tree.selection()

        if not seleccion:
             return messagebox.showwarning("Advertencia","no se ha seleccionado ninguno producto para eliminar")
        
        valores = self.tree.item(seleccion[0])["values"]
        id_eliminar = valores[0]
        nombre = valores[1]
        precio = valores[2]
        cantidad= int(valores[3])

        if cantidad > 0:
               return messagebox.showerror("No permitido","No se puede eliminar este producto por que tiene stock")    
        else:
            confirmar = messagebox.askyesno(
                "Confirmar eliminacion",
                f"Estas seguro que quieres eliminar al usuario:\n"
                f"Nombre: {nombre}\n"
                f"Precio: {precio}\n"
                f"Cantidad: {cantidad}?"
            )

        if not confirmar:
            return

        self.tree.delete(seleccion[0])
        self.eliminar_dato_producto_csv(id_eliminar)
        messagebox.showinfo("Se elimino correctamente.","Bien")

    def eliminar_dato_producto_csv(self, id_eliminar):
        archivo = "productos.csv"
        filas = []

        with open(archivo, "r", newline="") as f:
            reader = csv.reader(f)
            for fila in reader:
                if not fila:
                    continue

                if fila[0] != str(id_eliminar):
                    filas.append(fila)

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas)
    

    def limpiar_campos(self):

        self.producto_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)

class TablaProductos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

                #Tabla Productos
        columnas = ("id","Nombre", "Precio", "Cantidad")
        self.tree = ttk.Treeview(self, columns = columnas, show= "headings")

        self.tree.heading("id", text = "ID")
        self.tree.heading("Nombre", text = "Nombre")
        self.tree.heading("Precio", text = "Precio")
        self.tree.heading("Cantidad", text = "Cantidad")

        self.tree.pack()
        #Tabla Productos
        self.cargar_productos()   

    def cargar_productos(self):
        archivo = "productos.csv"

        for item in self.tree.get_children():
            self.tree.delete(item)

        if os.path.exists(archivo):
            with open(archivo, "r", newline="") as f:
                reader = csv.reader(f)
                for fila in reader:
                    if not fila:
                        continue
                    self.tree.insert("", tk.END, values=fila)