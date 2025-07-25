const { crc32_receptor } = require('./receptor/receptor');

// Cadenas de prueba y CRCs generados por el emisor
const crcEmisor1 = "11001101001100110100000100001011"; // "Hola, este es un mensaje de prueba"
const crcEmisor2 = "10110001111001110000000011010001"; // "Hola este es un mensaje 1"
const crcEmisor3 = "10111101110010101001010000101011"; // "Este es un mensaje 2"
const crcEmisor4 = "01111001101000111000010001111000"; // "Y este es el mensaje 3"

// 1. **Prueba sin errores**: Pasar el CRC original sin cambios para cada mensaje

console.log("Prueba sin errores para el mensaje 1:");
crc32_receptor("Hola, este es un mensaje de prueba", crcEmisor1);

console.log("Prueba sin errores para el mensaje 2:");
crc32_receptor("Hola este es un mensaje 1", crcEmisor2);

console.log("Prueba sin errores para el mensaje 3:");
crc32_receptor("Este es un mensaje 2", crcEmisor3);

console.log("Prueba sin errores para el mensaje 4:");
crc32_receptor("Y este es el mensaje 3", crcEmisor4);


// 2. **Prueba con un error**: Modificar un bit manualmente en el CRC de "Hola, este es un mensaje de prueba"
let crcConError = crcEmisor1.slice(0, 30) + '1' + crcEmisor1.slice(31); // Cambiar un bit en la posición 30
console.log("\nPrueba con un error para el mensaje 1:");
crc32_receptor("Hola, este es un mensaje de prueba", crcConError);

// 3. **Prueba con dos errores**: Modificar dos bits en el CRC de "Hola este es un mensaje 1"
let crcConDosErrores = crcEmisor2.slice(0, 15) + '1' + crcEmisor2.slice(16, 25) + '1' + crcEmisor2.slice(26); // Cambiar dos bits en las posiciones 15 y 25
console.log("\nPrueba con dos errores para el mensaje 2:");
crc32_receptor("Hola este es un mensaje 1", crcConDosErrores);


// 4. **Prueba con un error en el mensaje 3**: Cambiar un bit manualmente en el CRC de "Este es un mensaje 2"
let crcConErrorMensaje3 = crcEmisor3.slice(0, 20) + '1' + crcEmisor3.slice(21); // Cambiar un bit en la posición 20
console.log("\nPrueba con un error para el mensaje 3:");
crc32_receptor("Este es un mensaje 2", crcConErrorMensaje3);

// 5. **Prueba con dos errores en el mensaje 4**: Cambiar dos bits manualmente en el CRC de "Y este es el mensaje 3"
let crcConDosErroresMensaje4 = crcEmisor4.slice(5, 15) + '1' + crcEmisor4.slice(16, 25) + '1' + crcEmisor4.slice(26); // Cambiar dos bits en las posiciones 5 y 15
console.log("\nPrueba con dos errores para el mensaje 4:");
crc32_receptor("Y este es el mensaje 3", crcConDosErroresMensaje4);
