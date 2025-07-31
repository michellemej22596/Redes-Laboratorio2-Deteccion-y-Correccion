import matplotlib.pyplot as plt

# Leer los resultados de las pruebas
resultados = []
with open('resultados.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # Asegúrate de que no esté vacío
            partes = line.strip().split(', ')
            if len(partes) == 3:  # Asegurarse de que se tengan tres elementos por línea
                try:
                    tamano = int(partes[0])  # Tamaño del mensaje
                    error = float(partes[1])  # Error
                    mensaje = partes[2]  # Mensaje (correcto o con error)
                    resultados.append((tamano, error, mensaje))  # Guardar en el resultado
                except ValueError:
                    print(f"Error al leer la línea: {line.strip()}")  # Si hay algún problema al convertir
            else:
                print(f"Línea no válida: {line.strip()}")  # Si no tiene el formato correcto

# Agrupar los resultados por tamaño de mensaje y probabilidad de error
tamanos = sorted(list(set([r[0] for r in resultados])))  # Tamaños únicos de mensaje ordenados
errores = sorted(list(set([r[1] for r in resultados])))  # Errores únicos

# Crear un diccionario para almacenar el rendimiento por error
resultados_por_error = {error: [] for error in errores}

# Contar los mensajes correctos y con errores por tamaño de mensaje y error
for error in errores:
    for tamano in tamanos:
        tiempos = [r[2] for r in resultados if r[1] == error and r[0] == tamano]
        correctos = len([tiempo for tiempo in tiempos if 'correcto' in tiempo])  # Mensajes correctos
        errores_count = len([tiempo for tiempo in tiempos if 'error' in tiempo])  # Mensajes con error
        total = correctos + errores_count
        if total > 0:
            porcentaje_correcto = correctos / total * 100  # Porcentaje de mensajes corregidos
            resultados_por_error[error].append(porcentaje_correcto)
        else:
            resultados_por_error[error].append(0)  # Si no hay datos, asignar 0

# Graficamos el rendimiento
plt.figure(figsize=(10, 6))

# Graficar para cada error
for error in errores:
    plt.plot(tamanos, resultados_por_error[error], label=f'Error {error}', marker='o')

plt.xlabel("Tamaño de mensaje")
plt.ylabel("Porcentaje de corrección")
plt.title("Rendimiento del algoritmo de corrección de errores")
plt.legend()
plt.grid(True)
plt.show()
