import matplotlib.pyplot as plt
import numpy as np

# Leer los resultados de las pruebas
resultados = []
with open('resultados.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Para evitar líneas vacías
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Debemos tener tamaño, error, mensaje
                tamano, error, mensaje = partes
                resultados.append((int(tamano), float(error), mensaje))  # Almacenar como tupla

# Agrupar los resultados por tamaño de mensaje y probabilidad de error
tamanos = list(set([r[0] for r in resultados]))
errores = list(set([r[1] for r in resultados]))

# Inicializar listas para correctos y errores
correctos_por_error = []
errores_por_error = []

# Agrupar los mensajes correctos y con error por probabilidad de error
for error in errores:
    correctos = sum(1 for r in resultados if r[1] == error and 'correcto' in r[2])
    errores_ = sum(1 for r in resultados if r[1] == error and 'error' in r[2])
    correctos_por_error.append(correctos)
    errores_por_error.append(errores_)

# Crear la gráfica de barras
width = 0.35  # Ancho de las barras
x = np.arange(len(errores))  # Ubicación de las barras

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width / 2, correctos_por_error, width, label='Correctos')
ax.bar(x + width / 2, errores_por_error, width, label='Errores')

ax.set_xlabel('Probabilidad de error')
ax.set_ylabel('Cantidad de mensajes')
ax.set_title('Mensajes correctos y con error por probabilidad de error')
ax.set_xticks(x)
ax.set_xticklabels(errores)
ax.legend()

plt.show()
