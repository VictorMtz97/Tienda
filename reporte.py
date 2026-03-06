import tkinter as tk
import os 
from tkinter import filedialog, messagebox
import webbrowser

class Reporte(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador

        tk.Label(self, text="Aqui van los reportes").pack(pady=10)

        self.btn_seleccionar = tk.Button(self, text="Seleccionar Carpeta", command=self.listar_pdf)
        self.btn_seleccionar.pack(pady=10)

        # Listbox para mostrar los PDFs
        self.listbox_archivos = tk.Listbox(self, width=50, height=10)
        self.listbox_archivos.pack(pady=10)

        # # Scrollbar para el Listbox
        # self.scrollbar = tk.Scrollbar(self)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # self.listbox.config(yscrollcommand=self.scrollbar.set)
        # self.scrollbar.config(command=self.listbox.yview)

        tk.Button(self,text="Abrir", command=self.abrir_archivo).pack(pady=10)

    carpeta_actual = ""
    
    def listar_pdf(self):
        global carpeta_actual
        ruta = filedialog.askdirectory()

        if not ruta:
            return
        carpeta_actual= ruta
        self.listbox_archivos.delete(0, tk.END)

        try:
            for archivo in os.listdir(ruta):
                if archivo .lower().endswith(".pdf"):
                    self.listbox_archivos.insert(tk.END, archivo)

                if self.listbox_archivos.size() ==0:
                    messagebox.showinfo("Información", "No se encontraron archivos PDF.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo acceder a la carpeta: {e}")

    def abrir_archivo(self):

        seleccion = self.listbox_archivos.curselection()

        if not seleccion:
             return messagebox.showwarning("Advertencia","no se ha seleccionado ninguno archivo")
        nombre_archivo= self.listbox_archivos.get(self.listbox_archivos.curselection())

        file_path = os.path.join(carpeta_actual, nombre_archivo)

        if os.path.exists(file_path):
            webbrowser.open(file_path)
        else:
            messagebox.showerror("Error", "El archivo no existe")

