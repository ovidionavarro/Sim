import csv
import events as e

SLT = 5
SRVs, CA, client_queue, FJ, BJ, ET, CxJ, client_in_time = e.events(SLT, 6, 0.7)

# Encabezado del CSV
encabezado = ["CA", "CxJ", "FJ", "BJ", "ET", "SLT", "SRVs"]

# Datos que deseas agregar al archivo CSV
nuevos_datos = [[CA, CxJ, FJ, BJ, ET, SLT, SRVs]]

# Ruta del archivo CSV
ruta_archivo_csv = 'data.csv'

# Abrir el archivo CSV en modo de agregado
with open(ruta_archivo_csv, 'a', newline='', encoding='utf-8') as archivo_csv:
    # Crear un objeto escritor CSV
    escritor_csv = csv.writer(archivo_csv, delimiter=';')

    # Si el archivo está vacío, escribir el encabezado
    if archivo_csv.tell() == 0:
        escritor_csv.writerow(encabezado)

    # Escribir los nuevos datos en el archivo CSV
    for fila in nuevos_datos:
        escritor_csv.writerow(fila)

