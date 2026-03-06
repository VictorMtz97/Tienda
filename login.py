import tkinter as tk
from tkinter import messagebox
from principal import Principal
import csv



class Login(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent,bg="#355872")
        self.controlador = controlador

        
        bg_color = "#9CD5FF"
        lbl_font = ("Segoe UI", 16)
        title_font = ("Segoe UI", 24, "bold")

        #Titulo
        self.label_texto1= tk.Label(self, text="INICIO DE SESIÓN", font=title_font, bg="#9CD5FF").pack(pady=(10, 40))

        #Usuario
        tk.Label(self, text="Usuario", font=lbl_font).pack()
        self.entry_usuario = tk.Entry(self, font=("Arial", 12), bd=0, highlightthickness=1)
        self.entry_usuario.pack(ipady=8, pady=(5, 20))

        #Contraseña
        self.label_texto3= tk.Label(self, text="Contraseña", font=lbl_font).pack()
        self.entry_pass = tk.Entry(self, show="*",font=("Arial", 12), bd=0, highlightthickness=1)
        self.entry_pass.pack(ipady=8, pady=(5, 10))

        self.check_var = tk.BooleanVar()

        check = tk.Checkbutton(self, text="Mostrar contraseña",variable=self.check_var,command=self.mostrar_password, bg=bg_color, fg="white", 
                           selectcolor="#050520", activebackground=bg_color, font = ("Segoe UI", 16) , 
                           activeforeground="white")
        check.pack(pady=(0, 30))

        self.boton_inicio= tk.Button(self, text="Iniciar sesion", command = self.verificar_usuario, font=("Segoe UI", 12, "bold"),
                      bg="#0078d7", fg="white", bd=0, cursor="hand2",
                      activebackground="#005a9e", activeforeground="white").pack(ipady=10)


    def verificar_usuario(self):

        usuario = self.entry_usuario.get()
        password = self.entry_pass.get()
        if usuario == "" and password== "":
             self.mostrar_principal()
        # try:
        #     with open("usuarios.csv", mode ="r", newline="", encoding="utf-8") as file:

        #         reader= csv.reader(file)   

        #         for row in reader:
        #             if row[1]== usuario and row[3]== password:
                        # self.mostrar_principal()
        #                 break   
        # except FileNotFoundError:
        #     print("Error: No se encontró el archivo 'usuarios.csv'.")
        #     return


    def mostrar_principal(self):
                
                self.pack_forget()
                self.frame_actual = Principal(self.master, self.controlador)
                self.frame_actual.pack(fill="both", expand=True)

    def mostrar_password(self):
        if self.check_var.get():
            self.entry_pass.config(show="")
        else:
            self.entry_pass.config(show="*")

            


