import matplotlib.pyplot as plt

# Leer los resultados de las pruebas para 10k
resultados_10k = []
with open('resultados10k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Para evitar líneas vacías
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Debemos tener tamaño, error, mensaje
                tamano, error, mensaje = partes
                resultados_10k.append((int(tamano), float(error), mensaje))  # Almacenar como tupla

# Leer los resultados de las pruebas para 20k
resultados_20k = []
with open('resultados20k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Para evitar líneas vacías
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Debemos tener tamaño, error, mensaje
                tamano, error, mensaje = partes
                resultados_20k.append((int(tamano), float(error), mensaje))  # Almacenar como tupla

# Función para contar mensajes correctos e incorrectos
def contar_mensajes(resultados):
    correctos = sum(1 for r in resultados if r[1] == 0.0 and 'correcto' in r[2])
    incorrectos = sum(1 for r in resultados if r[1] == 0.01 and 'error' in r[2])
    return correctos, incorrectos

# Contar mensajes para 10k y 20k
correctos_10k, incorrectos_10k = contar_mensajes(resultados_10k)
correctos_20k, incorrectos_20k = contar_mensajes(resultados_20k)

# Crear la gráfica de barras para 10k
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 10k
ax[0].bar(['Correctos', 'Incorrectos'], [correctos_10k, incorrectos_10k], color=['blue', 'orange'])
ax[0].set_title('Mensajes correctos e incorrectos (10k)')
ax[0].set_ylabel('Cantidad de mensajes')

# 20k
ax[1].bar(['Correctos', 'Incorrectos'], [correctos_20k, incorrectos_20k], color=['blue', 'orange'])
ax[1].set_title('Mensajes correctos e incorrectos (20k)')
ax[1].set_ylabel('Cantidad de mensajes')

plt.tight_layout()
plt.show()
