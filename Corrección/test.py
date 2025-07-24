import unittest
from Emisor import hamming_encode, hamming_decode 

class TestHamming(unittest.TestCase):

    def test_sin_errores(self):
        """Prueba sin errores en el código Hamming"""
        mensajes = ["101010", "11011011", "1111001001"]
        
        for mensaje in mensajes:
            print("-" * 50)
            print(f"Prueba sin errores para el mensaje: {mensaje}")
            
            # Emisor genera el código Hamming
            codigo_hamming = hamming_encode(mensaje)
            print(f"Código Hamming generado: {codigo_hamming}")
            
            # Receptor recibe el código Hamming y lo verifica
            codigo_recibido = hamming_decode(codigo_hamming)
            print(f"Código recibido: {codigo_recibido}")
            print("-" * 50)
            self.assertEqual(codigo_recibido, mensaje)  # No debe haber cambios

    def test_con_error(self):
        """Prueba con un error en el código Hamming"""
        mensajes = ["101010", "11011011", "1111001001"]
        
        for mensaje in mensajes:
            print("-" * 50)
            print(f"Prueba con un error para el mensaje: {mensaje}")
            
            # Emisor genera el código Hamming
            codigo_hamming = hamming_encode(mensaje)
            print(f"Código Hamming generado: {codigo_hamming}")

            # Modificar un bit aleatorio para simular un error
            codigo_con_error = list(codigo_hamming)
            random_index = 3  # Modificar un bit en una posición específica para simplificar
            codigo_con_error[random_index] = '1' if codigo_con_error[random_index] == '0' else '0'  # Cambiar el bit
            codigo_con_error = ''.join(codigo_con_error)
            print(f"Código con error (bit modificado en la posición {random_index}): {codigo_con_error}")

            # Receptor recibe el código Hamming con error y lo corrige
            codigo_recibido = hamming_decode(codigo_con_error)
            print(f"Código recibido (con error corregido): {codigo_recibido}")
            print("-" * 50)

            # Comprobamos que el código recibido después de la corrección sea igual al código original
            self.assertEqual(codigo_recibido, mensaje)  # El código corregido debe ser igual al original

    def test_con_dos_errores(self):
        """Prueba con dos errores en el código Hamming"""
        mensajes = ["101010", "11011011", "1111001001"]
        
        for mensaje in mensajes:
            print("-" * 50)
            print(f"Prueba con dos errores para el mensaje: {mensaje}")
            
            # Emisor genera el código Hamming
            codigo_hamming = hamming_encode(mensaje)
            print(f"Código Hamming generado: {codigo_hamming}")

            # Modificar dos bits aleatorios para simular dos errores
            codigo_con_dos_errores = list(codigo_hamming)
            random_index_1 = 3  # Modificar un bit en una posición específica
            random_index_2 = 5  # Modificar otro bit en una posición diferente
            codigo_con_dos_errores[random_index_1] = '1' if codigo_con_dos_errores[random_index_1] == '0' else '0'  # Cambiar el primer bit
            codigo_con_dos_errores[random_index_2] = '1' if codigo_con_dos_errores[random_index_2] == '0' else '0'  # Cambiar el segundo bit
            codigo_con_dos_errores = ''.join(codigo_con_dos_errores)
            print(f"Código con dos errores (bits modificados en las posiciones {random_index_1} y {random_index_2}): {codigo_con_dos_errores}")

            # Receptor recibe el código Hamming con dos errores y lo corrige
            codigo_recibido = hamming_decode(codigo_con_dos_errores)
            print(f"Código recibido (con dos errores corregidos): {codigo_recibido}")
            print("-" * 50)

            # Comprobamos que el código recibido después de la corrección NO sea igual al código original
            # Deberíamos esperar que se indique que no se puede corregir
            self.assertNotEqual(codigo_recibido, mensaje)  # No debe ser igual al original, ya que no se puede corregir

if __name__ == "__main__":
    unittest.main()
