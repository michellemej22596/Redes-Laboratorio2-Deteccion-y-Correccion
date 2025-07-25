// receptor.js

function crc32_receptor(datos, crcRecibido) {
    const CRC32_TABLE = new Array(256).fill(0);
    const polynomial = 0xEDB88320;

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

    let crc = 0xFFFFFFFF;
    for (let i = 0; i < datos.length; i++) {
        const byte = datos.charCodeAt(i);
        crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ byte) & 0xFF];
    }
    crc ^= 0xFFFFFFFF;

    const crcBin = (crc >>> 0).toString(2).padStart(32, '0');

    if (crcBin === crcRecibido) {
        console.log("La integridad del mensaje es válida.");
    } else {
        console.log("El mensaje ha sido corrompido.");
    }
}

// Exportamos la función
module.exports = {
    crc32_receptor
};
