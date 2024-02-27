#import random
#import math
#
#def tiempo_espera(lambda_llegada, lambda_servicio):
#    tiempos_llegada = [generar_exponencial(lambda_llegada)]
#    tiempos_servicio = [generar_exponencial(lambda_servicio)]
#    tiempos_espera = [max(0, tiempos_servicio[0] - tiempos_llegada[0])]
#
#    for i in range(1, len(tiempos_llegada)):
#        tiempo_llegada = tiempos_llegada[i]
#        tiempo_servicio = tiempos_servicio[i]
#
#        tiempos_espera.append(max(0, tiempos_servicio[i-1] + tiempos_espera[i-1] - tiempos_llegada[i]))
#
#    return tiempos_espera
#
#def generar_exponencial(lmbda):
#    u = random.random()
#    return -math.log(1 - u) / lmbda
#
## Parámetro de tasa de llegada y servicio (solicitudes por hora)
#lambda_llegada = 5  # Tasa de llegada de solicitudes
#lambda_servicio = 8  # Tasa de servicio de solicitudes
#
## Simulación de los tiempos de espera de un servidor
#tiempos_espera = tiempo_espera(lambda_llegada, lambda_servicio)
#
## Imprimir los tiempos de espera de cada solicitud
#for i, tiempo in enumerate(tiempos_espera):
#    print(f'Tiempo de espera de solicitud {i+1}: {tiempo:.2f} horas')
#print(60*24)

import random
import math

def llegadas_minutos_poisson(lambda_value):
    tiempos_llegada = []
    tiempo_actual = 0
    while tiempo_actual < 1440:  # Simulamos un día de 1440 minutos
        tiempo_entre_llegadas = generar_poisson(lambda_value)
        tiempo_actual += tiempo_entre_llegadas
        if tiempo_actual < 1440:
            tiempos_llegada.append(tiempo_actual)
            
    return tiempos_llegada

def generar_poisson(lmbda):
    L = math.exp(-lmbda)
    k = 0
    p = 1.0

    while p > L:
        k = k + 1
        u = random.random()
        p = p * u

    return k - 1

# Parámetro de tasa de llegada (clientes por minuto)
lambda_value = 5  # Por ejemplo, 0.1 cliente por minuto

# Simulación de las llegadas de clientes durante un día (1440 minutos) con distribución de Poisson
llegadas_poisson = llegadas_minutos_poisson(lambda_value)

# Imprimir los tiempos de llegada de cada cliente en formato de minutos
for i, tiempo in enumerate(llegadas_poisson):
    print(f'Cliente {i+1} llega en el minuto: {tiempo:.2f}')