import tkinter as tk

class Reporte(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador

        tk.Label(self, text="Aqui van los reportes").pack(pady=10)