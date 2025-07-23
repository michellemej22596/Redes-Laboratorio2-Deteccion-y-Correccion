function crc32_receptor(datos, crcRecibido) {
    // Tabla de CRC-32 generada previamente
    const CRC32_TABLE = new Array(256).fill(0);
    const polynomial = 0xEDB88320;

    // Rellenamos la tabla CRC-32
    for (let i = 0; i < 256; i++) {
        let crc = i;
        for (let j = 0; j < 8; j++) {
            if (crc & 1) {
                crc = (crc >>> 1) ^ polynomial;
            } else {
                crc >>>= 1;
            }
        }
        CRC32_TABLE[i] = crc;
    }

    // Calculamos el CRC-32 del mensaje recibido
    let crc = 0xFFFFFFFF;
    for (let i = 0; i < datos.length; i++) {
        const byte = datos.charCodeAt(i);
        crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ byte) & 0xFF];
    }

    crc ^= 0xFFFFFFFF;

    // Convertimos el CRC calculado a una cadena binaria de 32 bits
    const crcBin = (crc >>> 0).toString(2).padStart(32, '0');

    // Comprobamos si el CRC calculado coincide con el CRC recibido
    if (crcBin === crcRecibido) {
        console.log("La integridad del mensaje es válida.");
    } else {
        console.log("El mensaje ha sido corrompido.");
    }
}

// Ejemplo
const mensajeRecibido = "Hola, este es un mensaje de prueba";
const crcEnviado = "11001101001100110100000100001011";

crc32_receptor(mensajeRecibido, crcEnviado);
