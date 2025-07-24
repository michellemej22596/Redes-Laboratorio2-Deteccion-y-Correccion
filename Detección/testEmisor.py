from emisor import crc32_emisor

def probar_emisor():
    # Tres cadenas de prueba
    mensajes = ["Hola este es un mensaje 1", "Este es un mensaje 2", "Y este es el mensaje 3"]

    for mensaje in mensajes:
        print("-" * 50)
        print(f"Mensaje original: {mensaje}")

        # Emisor genera el CRC-32
        crc_calculado = crc32_emisor(mensaje)
        print(f"CRC-32 calculado por el emisor (en binario): {crc_calculado}")
        print("-" * 50)

if __name__ == "__main__":
    probar_emisor()
