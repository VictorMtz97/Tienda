import tkinter as tk
from  tkinter import ttk
from productos import TablaProductos
from tkinter import messagebox



class Ventas(tk.Frame ):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador

        tk.Label(self, text="Aqui van el cajero").pack(pady=10)
        tk.Button(self, text="Añadir", command=self.añadir_carrito).pack(pady=10)
        tk.Button(self, text="Limpiar", command=self.limpiar_campos).pack(pady=10)

        frame_tablas= tk.Frame(self)
        frame_tablas.pack(fill="y")

        #Tabla de productos
        self.tabla_productos = TablaProductos(frame_tablas)
        self.tabla_productos.pack(side="left", fill="y", pady=10)
        #Tabla de productos

        #Tabla Carrito
        columnas = ("nombre","precio")
        self.tabla_carrito = ttk.Treeview(frame_tablas, columns = columnas, show= "headings")
        self.tabla_carrito.heading("nombre", text = "Nombre")
        self.tabla_carrito.heading("precio", text = "Precio")
        self.tabla_carrito.column("nombre", width=150, anchor="center")
        self.tabla_carrito.column("precio", width=100, anchor="center")
        self.tabla_carrito.pack(side="left", fill="y", padx=10)
        #Tabla Carrito

    def añadir_carrito(self):
        seleccion = self.tabla_productos.tree.selection()
        if not seleccion:
             return messagebox.showwarning("Advertencia","no se ha seleccionado ninguno para eliminar")
        
        valores = self.tabla_productos.tree.item(seleccion[0])["values"]

        nombre = valores[1]
        precio = valores[2]
        stock = valores[3]

        if stock <= 0:
            messagebox.showerror("Sin stock", "Este producto no tiene stock")
            return
        self.tabla_carrito.insert("", tk.END, values= (nombre,precio))

    def limpiar_campos(self):
        if not self.tabla_carrito.get_children():
            messagebox.showinfo("Carrito Vacio","No hay productos en el carrito")
            return
        confirmar= messagebox.askyesno("Confirmar", "Estas seguro que quieres vaciar el carrito?")
        if not confirmar:
            return
        self.tabla_carrito.delete(*self.tabla_carrito.get_children())
        messagebox.showinfo("Listo", "El carrito se vació correctamente.")


        
