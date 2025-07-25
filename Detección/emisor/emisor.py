import socket
from crc32 import crc32_emisor  # Importa la función CRC-32 del archivo crc32.py

# Datos del mensaje
mensaje = "Hola, este es un mensaje de prueba"
crc_calculado = crc32_emisor(mensaje)  # Calcula el CRC del mensaje

HOST = "127.0.0.1"  # IP de destino (localhost)
PORT = 65432  # Puerto donde se escuchará la conexión

# Crea el socket y lo conecta al receptor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conecta al receptor

    # Envía el mensaje y el CRC al receptor
    mensaje_con_crc = f"{mensaje}::{crc_calculado}"
    s.sendall(mensaje_con_crc.encode())  # Envía el mensaje como bytes

    # Recibe la respuesta del receptor (si la hay)
    data = s.recv(1024)
    print(f"Recibido: {data.decode()}")
