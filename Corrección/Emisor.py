import socket
import random

# Función para convertir texto a binario
def convertir_a_binario(mensaje):
    return ''.join(format(ord(c), '08b') for c in mensaje)

def hamming_encode(data):
    data_len = len(data)
    r = 0
    while (2**r) < (data_len + r + 1):
        r += 1

    encoded_data = [0] * (data_len + r)
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if (i & (i - 1)) == 0:
            continue
        else:
            encoded_data[i-1] = int(data[j])
            j += 1
    
    for parity_bit in range(r):
        parity_index = 2**parity_bit
        parity_value = 0
        for i in range(1, len(encoded_data) + 1):
            if (i >> parity_bit) & 1:
                parity_value ^= encoded_data[i-1]
        encoded_data[parity_index-1] = parity_value

    return "".join(map(str, encoded_data))

# Clase que maneja el enlace (Integridad)
class EmisorEnlace:
    def calcular_integridad(self, mensaje):
        return hamming_encode(mensaje)  # Usando la misma función de Hamming

class EmisorRuido:
    def aplicar_ruido(self, mensaje_codificado, errores_maximos=1):
        """Introduce un número limitado de errores (bits volteados aleatoriamente)."""
        mensaje_list = list(mensaje_codificado)
        if errores_maximos > 0:
            indices = random.sample(range(len(mensaje_list)), min(errores_maximos, len(mensaje_list)))
            for i in indices:
                mensaje_list[i] = '1' if mensaje_list[i] == '0' else '0'
        return ''.join(mensaje_list)

# Clase que maneja la aplicación del Emisor
class EmisorAplicacion:
    def __init__(self):
        self.mensaje = ""
    
    def solicitar_mensaje(self):
        """Solicita el mensaje a enviar."""
        self.mensaje = input("Ingrese el mensaje a enviar: ")
    
    def mostrar_mensaje(self):
        """Muestra el mensaje final después de ser codificado y con posibles errores."""
        print("Mensaje original:", self.mensaje)

class EmisorPresentacion:
    def codificar_mensaje(self, mensaje):
        """Codifica el mensaje en binario con Hamming por bloques de 4 bits."""
        mensaje_binario = convertir_a_binario(mensaje)
        
        # Padding si no múltiplo de 4
        while len(mensaje_binario) % 4 != 0:
            mensaje_binario += '0'
        
        bloques = [mensaje_binario[i:i+4] for i in range(0, len(mensaje_binario), 4)]
        bloques_codificados = [hamming_encode(bloque) for bloque in bloques]
        
        return ''.join(bloques_codificados)

# Ejemplo de ejecución del Emisor con Socket
def emisor_socket(mensaje):
    # Codificación del mensaje
    presentacion = EmisorPresentacion()
    mensaje_codificado = presentacion.codificar_mensaje(mensaje)
    print("Mensaje codificado:", mensaje_codificado)
    
    # Aplicar ruido con solo 1 bit de error
    ruido = EmisorRuido()
    mensaje_con_ruido = ruido.aplicar_ruido(mensaje_codificado, errores_maximos=1)

    
    # Mostrar el mensaje final
    print("Mensaje final con ruido:", mensaje_con_ruido)
    
    # Conectar al servidor (receptor) utilizando un socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))  # Cambia el puerto si es necesario
    
    # Enviar el mensaje codificado con ruido al receptor
    client_socket.send(mensaje_con_ruido.encode("utf-8"))
    
    # Cerrar la conexión
    client_socket.close()

if __name__ == "__main__":
    emisor = EmisorAplicacion()
    emisor.solicitar_mensaje()  # Solicita al usuario ingresar el mensaje.
    
    # Llamada a la función que maneja la transmisión con socket
    emisor_socket(emisor.mensaje)
