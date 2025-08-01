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
                    tamano, error, resultado = partes
                    resultados.append((int(tamano), float(error), resultado))
except FileNotFoundError:
    print("Archivo resultados_crc32.txt no encontrado. Ejecuta primero las pruebas automatizadas.")
    exit(1)

# Agrupar los resultados por probabilidad de error
errores = sorted(list(set([r[1] for r in resultados])))

# Inicializar contadores
datos_por_error = {}
for error in errores:
    datos_por_error[error] = {
        'correctos': 0,
        'errores_detectados': 0,
        'errores_no_detectados': 0,
        'falsos_positivos': 0
    }

# Contar los diferentes tipos de resultados
for tamano, error, resultado in resultados:
    if 'mensaje correcto' in resultado:
        datos_por_error[error]['correctos'] += 1
    elif 'error detectado correctamente' in resultado:
        datos_por_error[error]['errores_detectados'] += 1
    elif 'error no detectado' in resultado:
        datos_por_error[error]['errores_no_detectados'] += 1
    elif 'falso positivo' in resultado:
        datos_por_error[error]['falsos_positivos'] += 1

# Crear gráfico de barras agrupadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Distribución general por probabilidad de error
width = 0.2
x = np.arange(len(errores))

correctos = [datos_por_error[error]['correctos'] for error in errores]
detectados = [datos_por_error[error]['errores_detectados'] for error in errores]
no_detectados = [datos_por_error[error]['errores_no_detectados'] for error in errores]
falsos_pos = [datos_por_error[error]['falsos_positivos'] for error in errores]

ax1.bar(x - 1.5*width, correctos, width, label='Mensajes correctos', color='green', alpha=0.8)
ax1.bar(x - 0.5*width, detectados, width, label='Errores detectados', color='blue', alpha=0.8)
ax1.bar(x + 0.5*width, no_detectados, width, label='Errores NO detectados', color='red', alpha=0.8)
ax1.bar(x + 1.5*width, falsos_pos, width, label='Falsos positivos', color='orange', alpha=0.8)

ax1.set_xlabel('Probabilidad de error')
ax1.set_ylabel('Cantidad de mensajes')
ax1.set_title('Distribución de resultados por probabilidad de error')
ax1.set_xticks(x)
ax1.set_xticklabels([f'{error:.2f}' for error in errores])
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Eficacia de detección (porcentajes)
eficacia_deteccion = []
for error in errores:
    total_con_error = datos_por_error[error]['errores_detectados'] + datos_por_error[error]['errores_no_detectados']
    if total_con_error > 0:
        eficacia = (datos_por_error[error]['errores_detectados'] / total_con_error) * 100
    else:
        eficacia = 100  # Si no hay errores, la eficacia es perfecta
    eficacia_deteccion.append(eficacia)

ax2.bar(range(len(errores)), eficacia_deteccion, color='skyblue', alpha=0.8)
ax2.set_xlabel('Probabilidad de error')
ax2.set_ylabel('Eficacia de detección (%)')
ax2.set_title('Eficacia de detección de errores CRC32')
ax2.set_xticks(range(len(errores)))
ax2.set_xticklabels([f'{error:.2f}' for error in errores])
ax2.set_ylim(0, 105)
ax2.grid(True, alpha=0.3)

# Añadir valores en las barras del segundo gráfico
for i, v in enumerate(eficacia_deteccion):
    ax2.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# Mostrar estadísticas detalladas
print("\n=== ESTADÍSTICAS DETALLADAS CRC32 ===")
for error in errores:
    print(f"\nProbabilidad de error: {error}")
    print(f"  Mensajes correctos: {datos_por_error[error]['correctos']}")
    print(f"  Errores detectados correctamente: {datos_por_error[error]['errores_detectados']}")
    print(f"  Errores NO detectados: {datos_por_error[error]['errores_no_detectados']}")
    print(f"  Falsos positivos: {datos_por_error[error]['falsos_positivos']}")
    
    total_con_error = datos_por_error[error]['errores_detectados'] + datos_por_error[error]['errores_no_detectados']
    if total_con_error > 0:
        eficacia = (datos_por_error[error]['errores_detectados'] / total_con_error) * 100
        print(f"  Eficacia de detección: {eficacia:.2f}%")
