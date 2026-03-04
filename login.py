import tkinter as tk
from tkinter import messagebox
from principal import Principal


class Login(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent,bg="#050034")
        self.controlador = controlador
        self.label_texto1= tk.Label(self, text="Inicio de sesion").pack(pady=10)

        tk.Label(self, text="Usuario").pack()
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=10)

        self.label_texto3= tk.Label(self, text="Contraseña").pack()
        self.entry_pass = tk.Entry(self)
        self.entry_pass.pack(pady=10)

        self.boton_inicio= tk.Button(self, text="Iniciar sesion", command = self.verificar_usuario).pack()


    def verificar_usuario(self):

        usuario = self.entry_usuario.get()
        password = self.entry_pass.get()

        if usuario == "" and password == "":
            self.mostrar_principal()
        else:
            messagebox.showinfo("Error", "Inicio de sesion incorrecto.")


    def mostrar_principal(self):
                
                self.pack_forget()
                self.frame_actual = Principal(self.master, self.controlador)
                self.frame_actual.pack(fill="both", expand=True)

            


