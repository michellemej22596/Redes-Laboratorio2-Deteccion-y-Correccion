const assert = require('assert');
const { generarCodigoHamming, corregirHamming } = require('./Receptor');  // Importamos las funciones

// Test sin errores
describe('Pruebas Hamming', function() {
    it('Debería devolver el mensaje original sin errores', function() {
        // Tres mensajes con diferente longitud
        const mensajes = ["101010", "11011011", "1111001001"];
        
        mensajes.forEach(mensaje => {
            // Emisor genera el código Hamming
            const codigo_hamming = generarCodigoHamming(mensaje);
            // Receptor recibe el código Hamming y lo verifica
            const codigo_recibido = corregirHamming(codigo_hamming);
            assert.strictEqual(codigo_recibido, codigo_hamming);  // No debe haber cambios
        });
    });
});
