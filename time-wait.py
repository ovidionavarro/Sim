import random
import math
#
# def tiempo_espera(lambda_llegada, lambda_servicio):
#     tiempos_llegada = [generar_exponencial(lambda_llegada)]
#     tiempos_servicio = [generar_exponencial(lambda_servicio)]
#     tiempos_espera = [max(0, tiempos_servicio[0] - tiempos_llegada[0])]
#
#     for i in range(1, len(tiempos_llegada)):
#         tiempo_llegada = tiempos_llegada[i]
#         tiempo_servicio = tiempos_servicio[i]
#
#         tiempos_espera.append(max(0, tiempos_servicio[i-1] + tiempos_espera[i-1] - tiempos_llegada[i]))
#
#     return tiempos_espera
#
# def generar_exponencial(lmbda):
#     u = random.random()
#     return -math.log(1 - u) / lmbda
#
# # Parámetro de tasa de llegada y servicio (solicitudes por hora)
# lambda_llegada = 5  # Tasa de llegada de solicitudes
# lambda_servicio = 8  # Tasa de servicio de solicitudes
#
# # Simulación de los tiempos de espera de un servidor
# tiempos_espera = tiempo_espera(lambda_llegada, lambda_servicio)
#
# # Imprimir los tiempos de espera de cada solicitud
# for i, tiempo in enumerate(tiempos_espera):
#     print(f'Tiempo de espera de solicitud {i+1}: {tiempo:.2f} horas')