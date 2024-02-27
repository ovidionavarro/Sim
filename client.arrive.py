import random
import math

def llegada_siguiente(lmbda):
    u = random.random()
    tiempo_llegada = -math.log(1 - u) / lmbda
    return tiempo_llegada

# Parámetro de la tasa de llegada (clientes por hora)
lmbda = 5

# Simulación de tiempos entre llegadas de clientes al servidor
tiempo_actual = 0
for _ in range(10):
    tiempo_entre_llegadas = llegada_siguiente(lmbda)
    tiempo_actual += tiempo_entre_llegadas
    print(f'Tiempo entre llegadas: {tiempo_entre_llegadas:.2f} horas - Próxima llegada en: {tiempo_actual:.2f} horas')
