import csv
import events as e





def generate(row):
# Encabezado del CSV
    HEADER = ["CA", "CxJ", "FJ", "BJ", "ET", "SLT", "SRVs"]

    # Ruta del archivo CSV
    ruta_archivo_csv = 'data.csv'

    # Abrir el archivo CSV en modo de agregado
    with open(ruta_archivo_csv, 'a', newline='', encoding='utf-8') as archivo_csv:
        # Crear un objeto escritor CSV
        escritor_csv = csv.writer(archivo_csv, delimiter=';')

        # Si el archivo está vacío, escribir el encabezado
        if archivo_csv.tell() == 0:
            escritor_csv.writerow(HEADER)

        # Escribir los nuevos datos en el archivo CSV
        for fila in row:
            escritor_csv.writerow(fila)

