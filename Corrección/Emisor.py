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
    k = 0
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
    Decodifica los datos codificados con Hamming y detecta errores.
    """
    encoded_data = list(map(int, list(encoded_data)))
    r = 0
    data_len = len(encoded_data)
    while (2**r) < data_len:
        r += 1

    error_bit_pos = 0
    for parity_bit in range(r):
        parity_index = 2**parity_bit
        parity_value = 0
        for i in range(1, data_len + 1):
            if (i >> parity_bit) & 1:
                parity_value ^= encoded_data[i-1]
        if parity_value != 0:
            error_bit_pos += parity_index

    if error_bit_pos != 0:
        encoded_data[error_bit_pos-1] ^= 1
        print(f"Error detectado y corregido en la posición: {error_bit_pos}")

    decoded_data = ""
    for i in range(1, data_len + 1):
        if (i & (i-1)) != 0:
            decoded_data += str(encoded_data[i-1])

    return decoded_data
    
# Ejemplo de uso
data = "1011001"
encoded_data = hamming_encode(data)
print(f"Datos originales: {data}")
print(f"Datos codificados con Hamming: {encoded_data}")

# Simulando un error
error_index = 3
if error_index < len(encoded_data):
  modified_data = list(encoded_data)
  modified_data[error_index] = '1' if modified_data[error_index] == '0' else '0'
  modified_data = "".join(modified_data)
  print(f"Datos con error simulado: {modified_data}")
  decoded_data = hamming_decode(modified_data)
  print(f"Datos decodificados: {decoded_data}")
else:
    print("Índice de error fuera de rango.")

# Decodificando sin error
print(f"Datos decodificados sin error: {hamming_decode(encoded_data)}")
