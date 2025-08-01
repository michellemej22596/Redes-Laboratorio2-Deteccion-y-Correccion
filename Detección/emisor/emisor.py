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

def aplicar_ruido_opcional():
    respuesta = input("¿Desea aplicar ruido al mensaje? (s/n): ").lower()
    return respuesta == 's'

# Capa de Presentación: Codificar mensaje a binario ASCII
def codificar_mensaje(mensaje):
    return ''.join(format(ord(c), '08b') for c in mensaje)

# Capa de Enlace: Calcular CRC o Hamming
def calcular_integridad(mensaje, algoritmo):
    if algoritmo == "crc32":
        return crc32_emisor(mensaje)  # CRC-32
    else:
        return "Algoritmo no soportado"  # Placeholder para Hamming

# Capa de Ruido: Introducir error en el mensaje
def aplicar_ruido(mensaje_binario, probabilidad=0.01):
    mensaje_ruidoso = list(mensaje_binario)
    for i in range(len(mensaje_binario)):
        if random.random() < probabilidad:  # Probabilidad de aplicar el error
            mensaje_ruidoso[i] = '1' if mensaje_binario[i] == '0' else '0'
    return ''.join(mensaje_ruidoso)

# Función para introducir errores en el CRC (para pruebas)
def introducir_error_crc(crc, num_errores=1):
    crc_list = list(crc)
    indices = random.sample(range(len(crc)), min(num_errores, len(crc)))
    for i in indices:
        crc_list[i] = '1' if crc_list[i] == '0' else '0'
    return ''.join(crc_list)

# Función principal: Transmitir el mensaje
def emisor():
    mensaje = solicitar_mensaje()
    algoritmo = solicitar_algoritmo()

    # Codificar mensaje
    mensaje_binario = codificar_mensaje(mensaje)

    # Calcular CRC o Hamming
    crc_calculado = calcular_integridad(mensaje, algoritmo)

    # Preguntar si se debe aplicar ruido
    if aplicar_ruido_opcional():
        # Si elige "sí", se aplica el ruido al CRC
        crc_con_ruido = introducir_error_crc(crc_calculado)
        print("Ruido aplicado al CRC.")
    else:
        # Si elige "no", se envía el CRC sin ruido
        crc_con_ruido = crc_calculado
        print("No se aplicó ruido al CRC.")

    # Imprimir resultados
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje codificado en binario: {mensaje_binario}")
    print(f"CRC-32 calculado (binario): {crc_calculado}")
    print(f"CRC-32 enviado (binario): {crc_con_ruido}")

    # Establecer conexión con el receptor y enviar el mensaje con el CRC
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 65432))  # Conectamos al receptor
            mensaje_con_crc = f"{mensaje}::{crc_con_ruido}"  # Formato: mensaje::CRC
            s.sendall(mensaje_con_crc.encode())  # Enviar mensaje y CRC
            data = s.recv(1024)
            print(f"Respuesta del receptor: {data.decode()}")
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al receptor. Asegúrate de que esté ejecutándose.")
    except Exception as e:
        print(f"Error en la transmisión: {e}")

# Función para pruebas automatizadas
def emisor_automatizado(mensaje, introducir_error=False):
    """Versión automatizada del emisor para pruebas"""
    crc_calculado = crc32_emisor(mensaje)
    
    if introducir_error:
        crc_enviado = introducir_error_crc(crc_calculado)
    else:
        crc_enviado = crc_calculado
    
    return mensaje, crc_enviado

# Ejecutar el emisor
if __name__ == "__main__":
    emisor()
