import tkinter as tk
from login import Login


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de ventas")
        self.geometry("1200x800")
        self.mostrar_login()

    def mostrar_login(self):
        if hasattr(self, "frame_actual"):
            self.frame_actual.destroy()

        self.frame_actual = Login(self, self)
        self.frame_actual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()