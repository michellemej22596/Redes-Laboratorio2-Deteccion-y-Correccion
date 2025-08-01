"""
Script principal para ejecutar todas las pruebas de CRC32
"""

import subprocess
import sys

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y maneja errores"""
    print(f"\n{'='*50}")
    print(f"EJECUTANDO: {descripcion}")
    print(f"{'='*50}")

    try:
        if comando.endswith('.js'):
            # Para archivos JavaScript
            result = subprocess.run(['node', comando],
                                  capture_output=True,
                                  text=True,
                                  timeout=300)
        else:
            # Para archivos Python
            result = subprocess.run([sys.executable, comando],
                                  capture_output=True,
                                  text=True,
                                  timeout=300)

        if result.returncode == 0:
            print("ÉXITO")
            if result.stdout:
                print("Salida:")
                print(result.stdout)
        else:
            print("ERROR")
            if result.stderr:
                print("Error:")
                print(result.stderr)
            if result.stdout:
                print("Salida:")
                print(result.stdout)

    except subprocess.TimeoutExpired:
        print("IMEOUT - El proceso tardó demasiado")
    except FileNotFoundError:
        print(f"ARCHIVO NO ENCONTRADO: {comando}")
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")

def main():
    """Función principal que ejecuta todas las pruebas"""
    print("INICIANDO PRUEBAS COMPLETAS PARA CRC32")
    print("=" * 60)



    # 1. Ejecutar pruebas unitarias
    ejecutar_comando('test_crc32.py', 'Pruebas unitarias CRC32')

    # 2. Ejecutar pruebas automatizadas (esto puede tardar)
    print("\n Las pruebas automatizadas pueden tardar varios minutos...")
    ejecutar_comando('pruebas_automatizadas_crc32.js', 'Pruebas automatizadas CRC32')

    # 3. Generar gráficas de rendimiento
    ejecutar_comando('grafica_rendimiento_crc32.py', 'Gráfica de rendimiento')

    # 4. Generar gráfico de barras
    ejecutar_comando('grafico_barras_crc32.py', 'Gráfico de barras')

    print("\n" + "="*60)
    print("PRUEBAS COMPLETADAS")
    print("Revisa las gráficas generadas y el archivo resultados_crc32.txt")
    print("="*60)

if __name__ == "__main__":
    main()
