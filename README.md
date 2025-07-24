# Redes-Laboratorko2-Deteccion-y-Correccion
Silvia Illescas y Michelle Mejia

## **Descripción del Proyecto**

Este laboratorio tiene como objetivo analizar y aplicar diferentes algoritmos de detección y corrección de errores en la transmisión de datos. Se implementaron algoritmos de **CRC-32** para detección de errores y de **Hamming** para corrección. Ambos algoritmos fueron implementados en lenguajes diferentes para el emisor y receptor, y se realizaron pruebas de validación para asegurar su correcto funcionamiento.

## **Objetivos**

* Implementar y probar algoritmos de detección y corrección de errores.
* Comparar el comportamiento de los algoritmos CRC-32 y Hamming en distintos escenarios.
* Evaluar la capacidad de cada algoritmo para detectar y corregir errores en los datos.

## **Implementación**

* **Emisor CRC-32 (Python)**: Implementación del algoritmo CRC-32 para calcular el valor de verificación de integridad de un mensaje.
* **Receptor CRC-32 (JavaScript)**: Receptor que valida el CRC-32 calculado por el emisor y detecta errores de transmisión.
* **Emisor Hamming (Python)**: Implementación del algoritmo Hamming para la corrección de errores.
* **Receptor Hamming (JavaScript)**: Receptor que verifica y corrige los errores del mensaje usando el código Hamming.

## **Pruebas Realizadas**

1. **Pruebas sin errores**: Se enviaron mensajes sin modificaciones y se verificó que el receptor los validara correctamente.
2. **Pruebas con un error**: Se modificó un bit en el mensaje transmitido y se verificó si el receptor detectaba el error.
3. **Pruebas con dos o más errores**: Se modificaron dos o más bits y se comprobó si el receptor detectaba o corregía los errores.

## **Resultados**

Los resultados de las pruebas mostraron que:

* **CRC-32** es muy eficiente para la detección de errores, aunque en ciertos casos puede no detectar todos los tipos de errores si las modificaciones no son significativas.
* **Código Hamming** es efectivo para corregir errores simples, pero no puede corregir más de un error en un mensaje.

## **Ventajas y Desventajas**

* **CRC-32** tiene alta capacidad de detección y es adecuado para entornos con alta fiabilidad. Sin embargo, su complejidad y mayor overhead pueden no ser necesarios en sistemas simples.
* **Código Hamming** es muy simple de implementar y tiene bajo overhead, pero su capacidad de corrección es limitada a un solo error por mensaje.

## **Instrucciones de Uso**

1. **Clonar el Repositorio**:

   ```
   git clone https://github.com/michellemej22596/Redes-Laboratorio2-Deteccion-y-Correccion.git
   ```

2. **Ejecutar las Pruebas**:
   Para las pruebas del emisor y receptor en **Python** y **JavaScript**, simplemente ejecuta los siguientes comandos:

   **Python (emisor)**:

   ```
   python testEmisor.py
   ```

   **JavaScript (receptor)**:

   ```
   node testReceptor.js
   ```

3. **Requerimientos**:

   * Python 3.x
   * Node.js

