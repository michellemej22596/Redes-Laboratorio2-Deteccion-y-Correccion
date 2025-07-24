def hamming_encode(data):
    """
    Codifica los datos utilizando el código Hamming.
    """
    data_len = len(data)
    r = 0
    while (2**r) < (data_len + r + 1):
        r += 1

    encoded_data = [0] * (data_len + r)
    j = 0
    for i in range(1, len(encoded_data) + 1):
        if (i & (i - 1)) == 0:
            # Es potencia de 2, es un bit de paridad
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

def hamming_decode(encoded_data):
    """
    Decodifica los datos codificados con Hamming, detecta errores y corrige uno si es posible.
    Si hay más de un error, descarta el mensaje y notifica al usuario.
    """
    encoded_data = list(map(int, list(encoded_data)))  # Convertimos a lista de enteros
    r = 0  # Número de bits de paridad
    data_len = len(encoded_data)  # Longitud del mensaje codificado

    # Calcular el número de bits de paridad
    while (2**r) < data_len:
        r += 1

    error_bit_pos = 0  # Posición del bit con error
    errors_detected = 0  # Contador de errores detectados

    # Verificación de los bits de paridad para detectar errores
    for parity_bit in range(r):
        parity_index = 2**parity_bit
        parity_value = 0
        for i in range(1, data_len + 1):
            if (i >> parity_bit) & 1:
                parity_value ^= encoded_data[i-1]  # Comprobamos la paridad
        if parity_value != 0:
            error_bit_pos += parity_index  # Sumamos la posición de error
            errors_detected += 1  # Aumentamos el contador de errores detectados

    # Si más de un error se detecta, descartar el mensaje
    if errors_detected > 1:
        print(f"Se detectaron más de un error. El mensaje no se puede corregir.")
        return None  # Devuelve None o un valor que indique que no se puede corregir
    
    # Si hay un error, lo corregimos
    if error_bit_pos != 0:
        encoded_data[error_bit_pos-1] ^= 1  # Corregir el bit en la posición de error
        print(f"Error detectado y corregido en la posición: {error_bit_pos}")

    # Recuperar los datos decodificados eliminando los bits de paridad
    decoded_data = ""
    for i in range(1, data_len + 1):
        if (i & (i-1)) != 0:  # Solo recoger los bits de datos (que no son de paridad)
            decoded_data += str(encoded_data[i-1])

    return decoded_data

# Ejemplo de uso con tres mensajes diferentes
mensajes = ["1011001", "11011011", "1111001001"]
for mensaje in mensajes:
    encoded_data = hamming_encode(mensaje)
    print(f"Datos originales: {mensaje}")
    print(f"Datos codificados con Hamming: {encoded_data}")

    # Simulando un error
    error_index = 3
    modified_data = list(encoded_data)
    modified_data[error_index] = '1' if modified_data[error_index] == '0' else '0'
    modified_data = "".join(modified_data)
    print(f"Datos con error simulado: {modified_data}")
    decoded_data = hamming_decode(modified_data)
    print(f"Datos decodificados: {decoded_data}")

    # Simulando dos errores
    codigo_con_dos_errores = list(encoded_data)
    codigo_con_dos_errores[3] = '1' if codigo_con_dos_errores[3] == '0' else '0'  # Cambiar el primer bit
    codigo_con_dos_errores[5] = '1' if codigo_con_dos_errores[5] == '0' else '0'  # Cambiar el segundo bit
    codigo_con_dos_errores = ''.join(codigo_con_dos_errores)
    print(f"Datos con dos errores: {codigo_con_dos_errores}")
    decoded_data = hamming_decode(codigo_con_dos_errores)
    if decoded_data is None:
        print("El mensaje con dos errores no pudo ser corregido.")
    else:
        print(f"Datos decodificados (con dos errores corregidos): {decoded_data}")

    # Decodificando sin error
    print(f"Datos decodificados sin error: {hamming_decode(encoded_data)}")
