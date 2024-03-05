import tkinter as tk
import events as e
import generate_csv as g
from tkinter import messagebox


def start():
    servers = int(entry_servers.get())
    time = float(entry_time.get())
    umbral = float(entry_threshold.get())
    tests = int(entry_tests.get())

    if servers and time and umbral:
        if tests > 1:
            for i in range(tests):
                SRVs, CA, client_queue, FJ, BJ, ET, CxJ, client_in_time = e.events(int(servers), float(time),
                                                                                   float(umbral))
                g.generate([[CA, CxJ, FJ, BJ, ET, float(time), SRVs]])
        else:
            SRVs, CA, client_queue, FJ, BJ, ET, CxJ, client_in_time = e.events(int(servers), float(time), float(umbral))
            g.generate([[CA, CxJ, FJ, BJ, ET, float(time), SRVs]])

        messagebox.showinfo("Successful", "Simulation ended You can check on data.csv ")

    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Ingresar Datos")

# Establecer el tamaño de la ventana
ventana.geometry("300x150")  # Ancho x Alto en píxeles

# Crear etiquetas y campos de entrada
tk.Label(ventana, text="Servers:").grid(row=0, column=0)
entry_servers = tk.Entry(ventana)
entry_servers.grid(row=0, column=1)

tk.Label(ventana, text="Time:").grid(row=1, column=0)
entry_time = tk.Entry(ventana)
entry_time.grid(row=1, column=1)

tk.Label(ventana, text="Threshold:").grid(row=2, column=0)
entry_threshold = tk.Entry(ventana)
entry_threshold.grid(row=2, column=1)

tk.Label(ventana, text="Number of Test(With THIS data):").grid(row=3, column=0)
entry_tests = tk.Entry(ventana)
entry_tests.grid(row=3, column=1)

# Crear botón de inicio
boton_start = tk.Button(ventana, text="START Simulation!!!", command=start)
boton_start.grid(row=4, columnspan=2)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
