import tkinter as tk
from tkinter import messagebox

def iniciar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()

    if nombre and edad and ciudad:
        # Aquí puedes agregar el código para guardar los datos en el archivo CSV
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ingresar Datos")

# Crear etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Ciudad:").grid(row=2, column=0)
entry_ciudad = tk.Entry(ventana)
entry_ciudad.grid(row=2, column=1)

# Crear botón de inicio
boton_start = tk.Button(ventana, text="START", command=iniciar)
boton_start.grid(row=3, columnspan=2)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
