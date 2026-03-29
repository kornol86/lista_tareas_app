import tkinter as tk
from tkinter import messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # Evento doble clic
        self.lista.bind("<Double-1>", self.marcar_completada_evento)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.marcar_completada).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.listar_tareas():
            texto = str(tarea)
            self.lista.insert(tk.END, texto)

            # Cambiar color si está completada
            if tarea.completada:
                self.lista.itemconfig(tk.END, fg="gray")

    def agregar_tarea(self):
        descripcion = self.entry.get()
        if descripcion:
            self.servicio.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def obtener_id_seleccionado(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return None
        index = seleccion[0]
        tarea = self.servicio.listar_tareas()[index]
        return tarea.id

    def marcar_completada(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Seleccione una tarea")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.eliminar_tarea(id_tarea)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Seleccione una tarea")