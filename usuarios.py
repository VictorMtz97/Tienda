import tkinter as tk
from tkinter import ttk
import csv
import os
from tkinter import messagebox

class Usuarios(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent, bg="#355872")
        self.controlador = controlador


        tk.Label(self, text = "Aqui se registan los usuarios con el rol correspondiente.", font=("Segoe UI", 16)).pack(pady = 10)

        #Usuario
        tk.Label(self, text = "Usuario: ").pack(pady=10)
        self.user_entry = tk.Entry(self)
        self.user_entry.pack(pady=5)

        #Contraseña
        tk.Label(self, text = "Contraseña: ").pack(pady =10)
        self.pass_entry = tk.Entry(self)
        self.pass_entry.pack(pady = 5)

        #Radiobutton
        self.opcion_radio = tk.StringVar(value="")

        tk.Label(self, text = "Rol: ").pack(pady=10)
        tk.Radiobutton(self, text = "Administrador", variable=self.opcion_radio, value="Administrador").pack(pady=10)
        tk.Radiobutton(self, text = "Cajero", variable=self.opcion_radio, value="Cajero").pack(pady=10)

        #Botones
        tk.Button(self, text = "Añadir", command= self.agregar_usuarios, font=("Segoe", 12), fg="#000000", bg="#9CD5FF").pack(pady = 10)
        tk.Button(self, text = "Eliminar", command=self.eliminar_usuario, font=("Segoe", 12), fg="#000000", bg="#9CD5FF").pack(pady = 10)
        
        #Tabla
        columnas = ("id","rol", "usuario" )
        self.tree = ttk.Treeview(self, columns = columnas, show= "headings")

        self.tree.heading("id", text = "ID")
        self.tree.heading("usuario", text = "Usuario")
        self.tree.heading("rol", text = "Rol")

        self.tree.pack()
        #Tabla

        self.cargar_usuarios()



    def agregar_usuarios(self):
        
        usuario = self.user_entry.get()
        password = self.pass_entry.get()
        rol =  self.opcion_radio.get()

        if not usuario or not password or not rol:
           return messagebox.showwarning("Advertencia", "Te falto un dato revisa de nuevo")

        archivo="usuarios.csv"

        if os.path.exists(archivo):
            with open(archivo, "r", newline="") as f:
                reader= list(csv.reader(f))
                nuevo_id = len(reader)
        else:
            nuevo_id = 1

        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nuevo_id, usuario, rol, password])

        self.tree.insert("", tk.END, values=(nuevo_id, usuario, rol))

        self.limpiar_campos()

    def cargar_usuarios(self):
        archivo = "usuarios.csv"
        if os.path.exists(archivo):
            with open(archivo, "r", newline="") as f:
                reader = csv.reader(f)
                for fila in reader:
                    self.tree.insert("", tk.END, values=fila)

    def eliminar_usuario(self):
        seleccion = self.tree.selection()

        if not seleccion:
             return messagebox.showwarning("Advertencia","no se ha seleccionado ninguno para eliminar")
        
        valores = self.tree.item(seleccion[0])["values"]
        id_eliminar = valores[0]
        usuario = valores[1]
        rol = valores[2]

        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            f"Estas seguro que quieres eliminar al usuario:\n"
            f"Usuario: {usuario}\n"
            f"Rol: {rol}?"
        )

        if not confirmar:
            return

        self.tree.delete(seleccion[0])
        self.eliminar_dato_csv(id_eliminar)
        messagebox.showinfo("Se elimino correctamente.","Bien")

    def eliminar_dato_csv(self, id_eliminar):
        archivo = "usuarios.csv"
        filas = []

        with open(archivo, "r", newline="") as f:
            reader = csv.reader(f)
            for fila in reader:
                if fila[0] != str(id_eliminar):
                    filas.append(fila)

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas)



    def limpiar_campos(self):

        self.user_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.opcion_radio.set("")