function crc32_receptor(datos) {
    const CRC32_TABLE = new Array(256).fill(0);
    const polynomial = 0xEDB88320;

    // Generación de la tabla CRC-32
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
    
    // Recorrer cada carácter del mensaje para calcular el CRC
    for (let i = 0; i < datos.length; i++) {
        const byte = datos.charCodeAt(i);  // Obtener el código de carácter
        crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ byte) & 0xFF];  // Cálculo CRC
    }

    crc ^= 0xFFFFFFFF;  // Finalizar el cálculo del CRC

    // Retornar el CRC como una cadena binaria de 32 bits
    const crcBin = (crc >>> 0).toString(2).padStart(32, '0');  // Asegura 32 bits
    return crcBin;
}

module.exports = {
    crc32_receptor
};
