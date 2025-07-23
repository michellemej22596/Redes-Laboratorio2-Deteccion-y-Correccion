import unittest

def calcular_paridad(bits, pos):
    """Calcula el bit de paridad para una posición dada."""
    paridad = 0
    for i in range(len(bits)):
        if (i + 1) & pos:
            paridad ^= int(bits[i])  # XOR para obtener la paridad
    return str(paridad)

def generar_codigo_hamming(datos):
    """Genera el código Hamming para los datos de entrada."""
    datos = list(datos)
    
    # Calcular la cantidad de bits de paridad necesarios
    n = len(datos)
    m = 0
    while (2 ** m) < (n + m + 1):  # Número de bits de paridad
        m += 1
    
    # Inserta los bits de paridad
    hamming_code = [''] * (n + m)
    j = 0
    for i in range(1, n + m + 1):
        if (i & (i - 1)) == 0:  # Comprobamos si es una posición de bit de paridad
            hamming_code[i - 1] = '0'
        else:
            hamming_code[i - 1] = datos[j]
            j += 1
    
    # Asignar los valores a los bits de paridad
    for i in range(m):
        paridad_pos = 2 ** i
        paridad_bit = calcular_paridad(hamming_code, paridad_pos)
        hamming_code[paridad_pos - 1] = paridad_bit
    
    return ''.join(hamming_code)

def corregir_hamming(hammingCode):
    """Corrige el código Hamming recibido"""
    n = len(hammingCode)
    errorPos = 0
    for i in range(0, n):
        if (i + 1) & errorPos:
            errorPos += 2
    if errorPos != 0:
        hammingCode = (hammingCode[:errorPos-1] + 
                       ("1" if hammingCode[errorPos-1] == "0" else "0") +
                       hammingCode[errorPos:])
    return hammingCode

class TestHamming(unittest.TestCase):

    def test_sin_errores(self):
        # Tres mensajes con diferente longitud
        mensajes = ["101010", "11011011", "1111001001"]
        
        for mensaje in mensajes:
            # Emisor genera el código Hamming
            codigo_hamming = generar_codigo_hamming(mensaje)
            # Receptor recibe el código Hamming y lo verifica
            codigo_recibido = corregir_hamming(codigo_hamming)
            self.assertEqual(codigo_recibido, codigo_hamming)  # No debe haber cambios

if __name__ == "__main__":
    unittest.main()
