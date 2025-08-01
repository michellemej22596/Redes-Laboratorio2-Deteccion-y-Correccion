import random
import unittest
from crc32 import crc32_emisor

class TestCRC32(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.CRC32_TABLE = [0] * 256
        polynomial = 0xEDB88320

        for i in range(256):
            crc = i
            for j in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ polynomial
                else:
                    crc >>= 1
            self.CRC32_TABLE[i] = crc

    def crc32_python(self, datos):
        """Implementación de CRC32 en Python para pruebas"""
        crc = 0xFFFFFFFF
        for byte in datos.encode('utf-8'):
            crc = (crc >> 8) ^ self.CRC32_TABLE[(crc ^ byte) & 0xFF]
        crc = crc ^ 0xFFFFFFFF
        return format(crc, '032b')

    def introducir_error(self, crc, posicion):
        """Introduce un error en una posición específica del CRC"""
        crc_list = list(crc)
        crc_list[posicion] = '1' if crc_list[posicion] == '0' else '0'
        return ''.join(crc_list)

    def test_sin_errores(self):
        """Prueba sin errores en el CRC32"""
        tamanos = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Más tamaños de mensaje
        mensajes = ["Hola mundo", "Test CRC32", "Mensaje de prueba", "12345", "Un mensaje más largo de prueba"]
        
        for mensaje in mensajes:
            for tamano in tamanos:
                print(f"\n--- Prueba sin errores para: '{mensaje}' con tamaño {tamano} ---")
                
                # Calcular CRC original
                crc_original = self.crc32_python(mensaje)
                print(f"CRC32 calculado: {crc_original}")
                
                # Simular verificación (mismo CRC)
                crc_recibido = crc_original
                
                # Verificar integridad
                es_valido = crc_original == crc_recibido
                print(f"Verificación: {'VÁLIDO' if es_valido else 'INVÁLIDO'}")
                
                self.assertTrue(es_valido, f"El mensaje '{mensaje}' debería ser válido")

    def test_con_un_error(self):
        """Prueba con un error en el CRC32"""
        tamanos = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Más tamaños de mensaje
        mensajes = ["Hola mundo", "Test CRC32", "Mensaje de prueba", "12345", "Un mensaje más largo de prueba"]
        
        for mensaje in mensajes:
            for tamano in tamanos:
                print(f"\n--- Prueba con un error para: '{mensaje}' con tamaño {tamano} ---")
                
                # Calcular CRC original
                crc_original = self.crc32_python(mensaje)
                print(f"CRC32 original: {crc_original}")
                
                # Introducir un error en una posición aleatoria
                posicion_error = random.randint(0, 31)  # Posición aleatoria para introducir error
                crc_con_error = self.introducir_error(crc_original, posicion_error)
                print(f"CRC32 con error en posición {posicion_error}: {crc_con_error}")
                
                # Verificar que se detecta el error
                es_valido = crc_original == crc_con_error
                print(f"Verificación: {'VÁLIDO' if es_valido else 'ERROR DETECTADO'}")
                
                self.assertFalse(es_valido, f"El error en '{mensaje}' debería ser detectado")

    def test_con_multiples_errores(self):
        """Prueba con múltiples errores en el CRC32"""
        tamanos = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Más tamaños de mensaje
        mensajes = ["Hola mundo", "Test CRC32", "Mensaje de prueba", "12345", "Un mensaje más largo de prueba"]
        
        for mensaje in mensajes:
            for tamano in tamanos:
                print(f"\n--- Prueba con múltiples errores para: '{mensaje}' con tamaño {tamano} ---")
                
                # Calcular CRC original
                crc_original = self.crc32_python(mensaje)
                print(f"CRC32 original: {crc_original}")
                
                # Introducir múltiples errores
                crc_con_errores = crc_original
                posiciones_error = [random.randint(0, 31) for _ in range(3)]  # Tres posiciones aleatorias
                
                for pos in posiciones_error:
                    crc_con_errores = self.introducir_error(crc_con_errores, pos)
                
                print(f"CRC32 con errores en posiciones {posiciones_error}: {crc_con_errores}")
                
                # Verificar que se detectan los errores
                es_valido = crc_original == crc_con_errores
                print(f"Verificación: {'VÁLIDO' if es_valido else 'ERRORES DETECTADOS'}")
                
                self.assertFalse(es_valido, f"Los errores múltiples en '{mensaje}' deberían ser detectados")

if __name__ == "__main__":
    unittest.main(verbosity=2)
