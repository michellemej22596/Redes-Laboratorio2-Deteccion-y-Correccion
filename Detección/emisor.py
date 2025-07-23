def crc32_emisor(datos):
    # Tabla de CRC-32 generada previamente
    CRC32_TABLE = [0] * 256
    polynomial = 0xEDB88320

    # Rellenamos la tabla CRC-32
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        CRC32_TABLE[i] = crc

    # Calculamos el CRC-32 del mensaje
    crc = 0xFFFFFFFF
    for byte in datos.encode('utf-8'):
        crc = (crc >> 8) ^ CRC32_TABLE[(crc ^ byte) & 0xFF]

    crc = crc ^ 0xFFFFFFFF

    # Convertimos el CRC a una cadena binaria de 32 bits
    crc_bin = format(crc, '032b')
    return crc_bin

# Ejemplo de uso
mensaje = "Hola, este es un mensaje de prueba"
crc_enviado = crc32_emisor(mensaje)
print(f"Mensaje original: {mensaje}")
print(f"CRC-32 calculado por el emisor (en binario): {crc_enviado}")
