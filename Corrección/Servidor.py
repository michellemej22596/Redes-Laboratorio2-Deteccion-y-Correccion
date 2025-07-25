import socket

def hamming_decode(encoded_data):
    # Función de decodificación de Hamming que ya tienes.
    pass

def server():
    # Crear un socket para escuchar en localhost y puerto 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))  # Escuchar en localhost, puerto 12345
    server_socket.listen(1)
    
    print("Esperando conexión del emisor...")
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Recibir mensaje codificado
    encoded_message = client_socket.recv(1024).decode("utf-8")
    print(f"Mensaje recibido (con ruido): {encoded_message}")

    # Aquí deberías aplicar el proceso de decodificación, detección y corrección de errores.
    decoded_message = hamming_decode(encoded_message)
    if decoded_message is None:
        print("El mensaje tiene más de un error y no pudo ser corregido.")
    else:
        print(f"Mensaje decodificado correctamente: {decoded_message}")

    # Cerrar la conexión
    client_socket.close()

if __name__ == "__main__":
    server()
