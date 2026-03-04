import tkinter as tk
from tkinter import ttk
from ventas import Ventas
from usuarios import Usuarios
from productos import Productos
from reporte import Reporte
from productos import Productos


class Principal(tk.Frame,):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        self.label_texto_p = tk.Label(self, text="Pagina principal").pack(pady=10)

        self.notebook = ttk.Notebook(self)
        self.notebook.bind("<<NotebookTabChanged>>", self.actualizar_tablas)
        self.notebook.pack(fill="both", expand= True)

        self.frame_ventas = Ventas(self.notebook, controlador)
        self.frame_reportes = Reporte(self.notebook, controlador)
        self.frame_prodcutos = Productos(self.notebook, controlador)
        self.frame_usuarios = Usuarios(self.notebook, controlador)

        self.notebook.add(self.frame_ventas, text="Ventas")
        self.notebook.add(self.frame_reportes, text="Reportes")
        self.notebook.add(self.frame_prodcutos, text="Registro productos")
        self.notebook.add(self.frame_usuarios, text="Registro usuaios")

    def actualizar_tablas(self, event):
        pestaña_actual = event.widget.select()
        frame= event.widget.nametowidget(pestaña_actual)

        if hasattr(frame, "tabla"):
            frame.tabla.cargar_productos()


