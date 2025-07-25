import random
import socket
from crc32 import crc32_emisor  # Usando CRC-32 desde crc32.py

# Capa de Aplicación: Solicitar mensaje y algoritmo
def solicitar_mensaje():
    mensaje = input("Ingrese el mensaje a enviar: ")
    return mensaje

def solicitar_algoritmo():
    algoritmo = input("Seleccione el algoritmo (crc32/hamming): ").lower()
    return algoritmo

# Capa de Presentación: Codificar mensaje a binario ASCII
def codificar_mensaje(mensaje):
    return ''.join(format(ord(c), '08b') for c in mensaje)

# Capa de Enlace: Calcular CRC o Hamming
def calcular_integridad(mensaje, algoritmo):
    if algoritmo == "crc32":
        return crc32_emisor(mensaje)  # CRC-32
    else:
        return "Algoritmo no soportado"  # Placeholder para Hamming (implementarlo si es necesario)

# Capa de Ruido: Introducir error en el mensaje
def aplicar_ruido(mensaje_binario, probabilidad=0.01):
    mensaje_ruidoso = list(mensaje_binario)
    for i in range(len(mensaje_binario)):
        if random.random() < probabilidad:  # Probabilidad de aplicar el error
            mensaje_ruidoso[i] = '1' if mensaje_binario[i] == '0' else '0'
    return ''.join(mensaje_ruidoso)

# Función principal: Transmitir el mensaje
def emisor():
    mensaje = solicitar_mensaje()
    algoritmo = solicitar_algoritmo()

    # Codificar mensaje
    mensaje_binario = codificar_mensaje(mensaje)

    # Calcular CRC o Hamming
    crc_calculado = calcular_integridad(mensaje, algoritmo)

    # Aplicar ruido al mensaje binario
    mensaje_con_ruido = aplicar_ruido(mensaje_binario)

    # Imprimir resultados
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje codificado en binario: {mensaje_binario}")
    print(f"Mensaje con ruido (binario): {mensaje_con_ruido}")
    print(f"CRC-32 calculado (binario): {crc_calculado}")

    # Establecer conexión con el receptor y enviar el mensaje con el CRC
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 65432))  # Conectamos al receptor (localhost y puerto 65432)
        mensaje_con_crc = f"{mensaje}::{crc_calculado}"  # Formato: mensaje::CRC
        s.sendall(mensaje_con_crc.encode())  # Enviar mensaje y CRC
        data = s.recv(1024)
        print(f"Respuesta del receptor: {data.decode()}")

# Ejecutar el emisor
if __name__ == "__main__":
    emisor()
