const net = require("net")
const fs = require("fs")
const { crc32_receptor } = require("./receptor/crc32")

// Función para generar mensajes aleatorios de diferentes tamaños
function generarMensajeAleatorio(tamano) {
  const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
  let mensaje = ""
  for (let i = 0; i < tamano; i++) {
    mensaje += caracteres.charAt(Math.floor(Math.random() * caracteres.length))
  }
  return mensaje
}

// Función para calcular CRC32 (copiada del emisor)
function crc32_emisor(datos) {
  const CRC32_TABLE = new Array(256).fill(0)
  const polynomial = 0xedb88320

  for (let i = 0; i < 256; i++) {
    let crc = i
    for (let j = 0; j < 8; j++) {
      if (crc & 1) {
        crc = (crc >>> 1) ^ polynomial
      } else {
        crc >>>= 1
      }
    }
    CRC32_TABLE[i] = crc
  }

  let crc = 0xffffffff

  for (let i = 0; i < datos.length; i++) {
    const byte = datos.charCodeAt(i)
    crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ byte) & 0xff]
  }

  crc ^= 0xffffffff
  const crcBin = (crc >>> 0).toString(2).padStart(32, "0")
  return crcBin
}

// Función para introducir errores en el CRC
function introducirError(crc, numErrores = 1) {
  const crcArray = crc.split("")
  const indices = []

  // Seleccionar posiciones aleatorias para introducir errores
  while (indices.length < numErrores && indices.length < crc.length) {
    const indice = Math.floor(Math.random() * crc.length)
    if (!indices.includes(indice)) {
      indices.push(indice)
    }
  }

  // Invertir los bits en las posiciones seleccionadas
  indices.forEach((indice) => {
    crcArray[indice] = crcArray[indice] === "0" ? "1" : "0"
  })

  return crcArray.join("")
}

// Función para realizar una prueba individual
function realizarPrueba(mensaje, probabilidadError, tamano) {
  return new Promise((resolve) => {
    // Calcular CRC original
    const crcOriginal = crc32_emisor(mensaje)
    let crcEnviado = crcOriginal
    let tieneError = false

    // Decidir si introducir error basado en la probabilidad
    if (Math.random() < probabilidadError) {
      crcEnviado = introducirError(crcOriginal, 1)
      tieneError = true
    }

    // Simular la verificación del receptor
    const crcCalculado = crc32_receptor(mensaje)
    const esValido = crcCalculado === crcEnviado

    // Determinar el resultado
    let resultado
    if (tieneError && !esValido) {
      resultado = "error detectado correctamente"
    } else if (!tieneError && esValido) {
      resultado = "mensaje correcto"
    } else if (tieneError && esValido) {
      resultado = "error no detectado"
    } else {
      resultado = "falso positivo"
    }

    // Escribir resultado al archivo
    const linea = `${tamano}, ${probabilidadError}, ${resultado}\n`
    fs.appendFileSync("resultados_crc32.txt", linea)

    console.log(`Tamaño: ${tamano}, Error: ${probabilidadError}, Resultado: ${resultado}`)
    resolve(resultado)
  })
}

// Función principal para ejecutar todas las pruebas
async function ejecutarPruebas() {
  // Limpiar archivo de resultados
  fs.writeFileSync("resultados_crc32.txt", "")

  const tamanos = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
  const probabilidadesError = [0.0, 0.01, 0.02, 0.05]
  const pruebasPorConfiguracion = 100

  console.log("Iniciando pruebas automatizadas de CRC32...")

  for (const tamano of tamanos) {
    for (const probabilidad of probabilidadesError) {
      console.log(`\nProbando tamaño ${tamano} con probabilidad de error ${probabilidad}`)

      for (let i = 0; i < pruebasPorConfiguracion; i++) {
        const mensaje = generarMensajeAleatorio(tamano)
        await realizarPrueba(mensaje, probabilidad, tamano)

        // Pequeña pausa para no sobrecargar el sistema
        await new Promise((resolve) => setTimeout(resolve, 10))
      }
    }
  }

  console.log("\nPruebas completadas. Resultados guardados en resultados_crc32.txt")
}

// Ejecutar las pruebas
if (require.main === module) {
  ejecutarPruebas().catch(console.error)
}

module.exports = {
  generarMensajeAleatorio,
  crc32_emisor,
  introducirError,
  realizarPrueba,
  ejecutarPruebas,
}
