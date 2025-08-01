import matplotlib.pyplot as plt

# Leer los resultados de las pruebas para 10k
resultados_10k = []
with open('resultados10k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Asegúrate de que no esté vacío
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Asegurarse de que se tengan tres elementos por línea
                try:
                    tamano = int(partes[0])  # Tamaño del mensaje
                    error = float(partes[1])  # Error
                    mensaje = partes[2]  # Mensaje (correcto o con error)
                    resultados_10k.append((tamano, error, mensaje))  # Guardar en el resultado
                except ValueError:
                    print(f"Error al leer la línea: {line.strip()}")  # Si hay algún problema al convertir
            else:
                print(f"Línea no válida: {line.strip()}")  # Si no tiene el formato correcto

# Leer los resultados de las pruebas para 20k
resultados_20k = []
with open('resultados20k.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Asegúrate de que no esté vacío
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Asegurarse de que se tengan tres elementos por línea
                try:
                    tamano = int(partes[0])  # Tamaño del mensaje
                    error = float(partes[1])  # Error
                    mensaje = partes[2]  # Mensaje (correcto o con error)
                    resultados_20k.append((tamano, error, mensaje))  # Guardar en el resultado
                except ValueError:
                    print(f"Error al leer la línea: {line.strip()}")  # Si hay algún problema al convertir
            else:
                print(f"Línea no válida: {line.strip()}")  # Si no tiene el formato correcto

# Agrupar los resultados por tamaño de mensaje y probabilidad de error para ambos
tamanos_10k = sorted(list(set([r[0] for r in resultados_10k])))  # Tamaños únicos de mensaje ordenados para 10k
errores_10k = sorted(list(set([r[1] for r in resultados_10k])))  # Errores únicos para 10k

tamanos_20k = sorted(list(set([r[0] for r in resultados_20k])))  # Tamaños únicos de mensaje ordenados para 20k
errores_20k = sorted(list(set([r[1] for r in resultados_20k])))  # Errores únicos para 20k

# Crear diccionarios para almacenar el rendimiento por error
resultados_por_error_10k = {error: [] for error in errores_10k}
resultados_por_error_20k = {error: [] for error in errores_20k}

# Contar los mensajes correctos y con errores por tamaño de mensaje y error para 10k
for error in errores_10k:
    for tamano in tamanos_10k:
        tiempos = [r[2] for r in resultados_10k if r[1] == error and r[0] == tamano]
        correctos = len([tiempo for tiempo in tiempos if 'correcto' in tiempo])  # Mensajes correctos
        errores_count = len([tiempo for tiempo in tiempos if 'error' in tiempo])  # Mensajes con error
        total = correctos + errores_count
        if total > 0:
            porcentaje_correcto = correctos / total * 100  # Porcentaje de mensajes corregidos
            resultados_por_error_10k[error].append(porcentaje_correcto)
        else:
            resultados_por_error_10k[error].append(0)  # Si no hay datos, asignar 0

# Contar los mensajes correctos y con errores por tamaño de mensaje y error para 20k
for error in errores_20k:
    for tamano in tamanos_20k:
        tiempos = [r[2] for r in resultados_20k if r[1] == error and r[0] == tamano]
        correctos = len([tiempo for tiempo in tiempos if 'correcto' in tiempo])  # Mensajes correctos
        errores_count = len([tiempo for tiempo in tiempos if 'error' in tiempo])  # Mensajes con error
        total = correctos + errores_count
        if total > 0:
            porcentaje_correcto = correctos / total * 100  # Porcentaje de mensajes corregidos
            resultados_por_error_20k[error].append(porcentaje_correcto)
        else:
            resultados_por_error_20k[error].append(0)  # Si no hay datos, asignar 0

# Graficamos el rendimiento para 10k
plt.figure(figsize=(10, 6))

# Graficar para cada error en 10k
for error in errores_10k:
    plt.plot(tamanos_10k, resultados_por_error_10k[error], label=f'Error {error} 10k', marker='o')

plt.xlabel("Tamaño de mensaje")
plt.ylabel("Porcentaje de corrección")
plt.title("Rendimiento del algoritmo de corrección de errores (10k)")
plt.legend()
plt.grid(True)
plt.show()

# Graficamos el rendimiento para 20k
plt.figure(figsize=(10, 6))

# Graficar para cada error en 20k
for error in errores_20k:
    plt.plot(tamanos_20k, resultados_por_error_20k[error], label=f'Error {error} 20k', marker='x')

plt.xlabel("Tamaño de mensaje")
plt.ylabel("Porcentaje de corrección")
plt.title("Rendimiento del algoritmo de corrección de errores (20k)")
plt.legend()
plt.grid(True)
plt.show()
