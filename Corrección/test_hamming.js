const assert = require('assert');
const { generarCodigoHamming, corregirHamming } = require('./Receptor');  // Importar las funciones

// Test sin errores
describe('Pruebas Hamming', function() {
    it('Debería devolver el mensaje original sin errores', function() {
        // Tres mensajes con diferente longitud
        const mensajes = ["101010", "11011011", "1111001001"];
        
        mensajes.forEach(mensaje => {
            // Emisor genera el código Hamming
            const codigo_hamming = generarCodigoHamming(mensaje);
            console.log("Código Hamming generado: ", codigo_hamming);
            // Receptor recibe el código Hamming y lo verifica
            const codigo_recibido = corregirHamming(codigo_hamming);
            console.log("Código recibido: ", codigo_recibido);
            assert.strictEqual(codigo_recibido, codigo_hamming);  // No debe haber cambios
        });
    });

    // Test con un error
    it('Debería detectar y corregir el error en el bit', function() {
        // Tres mensajes con diferente longitud
        const mensajes = ["101010", "11011011", "1111001001"];
        
        mensajes.forEach(mensaje => {
            // Emisor genera el código Hamming
            const codigo_hamming = generarCodigoHamming(mensaje);
            console.log("Código Hamming generado: ", codigo_hamming);

            // Modificar un bit aleatorio para simular un error
            let codigo_con_error = codigo_hamming.split('');
            const randomIndex = Math.floor(Math.random() * codigo_con_error.length); // Generar un índice aleatorio
            codigo_con_error[randomIndex] = (codigo_con_error[randomIndex] === '0') ? '1' : '0';  // Cambiar el bit
            codigo_con_error = codigo_con_error.join('');
            console.log("Código con error: ", codigo_con_error);

            // Receptor recibe el código Hamming con error y lo corrige
            const codigo_recibido = corregirHamming(codigo_con_error);
            console.log("Código recibido (con error corregido): ", codigo_recibido);

            // Comprobamos que el código recibido después de la corrección sea igual al código original
            assert.strictEqual(codigo_recibido, codigo_hamming);  // El código corregido debe ser igual al original
        });
    });
});
