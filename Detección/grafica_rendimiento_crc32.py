import matplotlib.pyplot as plt
import numpy as np

# Leer los resultados de las pruebas
resultados = []
try:
    with open('resultados_crc32.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                partes = line.strip().split(', ')
                if len(partes) == 3:
                    try:
                        tamano = int(partes[0])
                        error = float(partes[1])
                        resultado = partes[2]
                        resultados.append((tamano, error, resultado))
                    except ValueError:
                        print(f"Error al leer la línea: {line.strip()}")
                else:
                    print(f"Línea no válida: {line.strip()}")
except FileNotFoundError:
    print("Archivo resultados_crc32.txt no encontrado. Ejecuta primero las pruebas automatizadas.")
    exit(1)

if not resultados:
    print("No se encontraron resultados válidos.")
    exit(1)

# Agrupar los resultados por tamaño de mensaje y probabilidad de error
tamanos = sorted(list(set([r[0] for r in resultados])))
errores = sorted(list(set([r[1] for r in resultados])))

# Crear un diccionario para almacenar el rendimiento por error
rendimiento_por_error = {error: [] for error in errores}

# Calcular el porcentaje de detección correcta por tamaño y probabilidad de error
for error in errores:
    for tamano in tamanos:
        resultados_filtrados = [r[2] for r in resultados if r[1] == error and r[0] == tamano]
        
        if resultados_filtrados:
            # Contar detecciones correctas
            correctos = len([r for r in resultados_filtrados if 'correcto' in r or 'detectado correctamente' in r])
            total = len(resultados_filtrados)
            porcentaje_correcto = (correctos / total) * 100
            rendimiento_por_error[error].append(porcentaje_correcto)
        else:
            rendimiento_por_error[error].append(0)

# Crear la gráfica de rendimiento
plt.figure(figsize=(12, 8))

# Graficar para cada probabilidad de error
for error in errores:
    if len(rendimiento_por_error[error]) == len(tamanos):
        plt.plot(tamanos, rendimiento_por_error[error], 
                label=f'Probabilidad de error: {error}', 
                marker='o', linewidth=2, markersize=6)

plt.xlabel("Tamaño de mensaje (caracteres)", fontsize=12)
plt.ylabel("Porcentaje de detección correcta (%)", fontsize=12)
plt.title("Rendimiento del algoritmo CRC32 para detección de errores", fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(0, 105)

# Mejorar el aspecto de la gráfica
plt.tight_layout()
plt.show()

# Mostrar estadísticas adicionales
print("\n=== ESTADÍSTICAS DE RENDIMIENTO CRC32 ===")
for error in errores:
    if rendimiento_por_error[error]:
        promedio = np.mean(rendimiento_por_error[error])
        print(f"Probabilidad de error {error}: {promedio:.2f}% de detección correcta promedio")
