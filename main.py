import tkinter as tk
from login import Login


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de ventas")
        # self.geometry("1200x800")
        ancho = 1200
        alto = 800
        pantalla_ancho = self.winfo_screenwidth() 
        pantalla_alto = self.winfo_screenheight()

        x = int((pantalla_ancho / 2) - (ancho / 2))
        y = int((pantalla_alto / 2) - (alto / 2))

        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.mostrar_login()

    def mostrar_login(self):
        if hasattr(self, "frame_actual"):
            self.frame_actual.destroy()

        self.frame_actual = Login(self, self)
        self.frame_actual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()