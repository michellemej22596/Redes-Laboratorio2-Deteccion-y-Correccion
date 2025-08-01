import random
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import time

# Función de CRC32 ya definida en crc32.py (emisor.py)
from crc32 import crc32_emisor

# Función para simular el ruido (errores)
def aplicar_ruido(mensaje, probabilidad_error):
    """Simula ruido en el mensaje alterando bits con una probabilidad dada"""
    mensaje_binario = ''.join(format(ord(c), '08b') for c in mensaje)  # Convertir mensaje a binario
    mensaje_ruido = list(mensaje_binario)
    
    for i in range(len(mensaje_ruido)):
        if random.random() < probabilidad_error:
            # Invertir el bit para simular el error
            mensaje_ruido[i] = '0' if mensaje_binario[i] == '1' else '1'
    
    return ''.join(mensaje_ruido)

# Función para realizar la prueba
def realizar_prueba(tamano_mensaje, probabilidad_error):
    """Realiza una prueba de transmisión, error y corrección con CRC32"""
    mensaje = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=tamano_mensaje))
    
    # Aplicar ruido al mensaje en un pequeño porcentaje de las pruebas
    aplicar_ruido_al_mensaje = random.random() < 0.01  # Solo el 1% de los mensajes tendrán ruido
    if aplicar_ruido_al_mensaje:
        mensaje_con_ruido = aplicar_ruido(mensaje, probabilidad_error)
    else:
        mensaje_con_ruido = mensaje  # Sin aplicar ruido

    # Calcular el CRC del mensaje original (emisor)
    crc_original = crc32_emisor(mensaje)
    
    # Simular la recepción del mensaje con el CRC (en JavaScript)
    try:
        result = subprocess.run(
            ['node', 'receptor.js', mensaje_con_ruido, crc_original],
            capture_output=True, text=True, timeout=10  # Timeout de 10 segundos
        )
        
        # Analizar el resultado
        if "La integridad del mensaje es válida." in result.stdout:
            return True  # Mensaje sin errores
        else:
            return False  # Mensaje con errores
    except subprocess.TimeoutExpired:
        print("El proceso ha superado el tiempo de espera")
        return False

# Realizar múltiples pruebas y almacenar los resultados
def realizar_pruebas(cant_pruebas, tamano_mensaje, probabilidad_error):
    exitosos = 0
    fallidos = 0
    
    for _ in range(cant_pruebas):
        if realizar_prueba(tamano_mensaje, probabilidad_error):
            exitosos += 1
        else:
            fallidos += 1
    
    return exitosos, fallidos

# Generar las gráficas con los resultados
def generar_grafica(resultados, tamano_mensaje, probabilidad_error):
    exitosos, fallidos = resultados
    total = exitosos + fallidos
    
    # Graficar los resultados
    plt.bar(['Exitosos', 'Fallidos'], [exitosos, fallidos], color=['green', 'red'])
    plt.title(f"Resultados de {tamano_mensaje} caracteres, Probabilidad de Error: {probabilidad_error}")
    plt.ylabel("Cantidad de mensajes")
    plt.show()

# Configuración de la prueba
cant_pruebas = 100
tamano_mensaje = 50  # Tamaño del mensaje (puedes ajustarlo)
probabilidad_error = 0.001  # Probabilidad de error (0.1%)

# Realizar las pruebas
resultados = realizar_pruebas(cant_pruebas, tamano_mensaje, probabilidad_error)

# Generar la gráfica
generar_grafica(resultados, tamano_mensaje, probabilidad_error)
