const fs = require('fs');
const net = require('net');

// Función para generar las pruebas
function pruebasAutomatizadas() {
    const mensajesPrueba = [
        "Hola",
        "Test",
        "Redes",
        "Hamming",
        "Codigo"
    ];

    // Crear o vaciar los archivos de resultados
    fs.writeFileSync('resultados10k.txt', '');
    fs.writeFileSync('resultados20k.txt', '');

    // Realizar las pruebas
    mensajesPrueba.forEach(mensaje => {
        // 1. Generar prueba sin error
        const mensajeBinario = convertirAMensajeBinario(mensaje);
        console.log(`\nProbando con mensaje sin error: "${mensaje}"`);
        console.log("Mensaje binario:", mensajeBinario);
        enviarMensaje(mensajeBinario, false, mensaje); // Sin error

        // 2. Generar prueba con error (introducimos un error en 1 bit)
        const mensajeConError = introducirError(mensajeBinario);
        console.log(`\nProbando con mensaje con error: "${mensaje}"`);
        console.log("Mensaje binario con error:", mensajeConError);
        enviarMensaje(mensajeConError, true, mensaje); // Con error
    });
}

// Función para convertir el mensaje en binario
function convertirAMensajeBinario(mensaje) {
    return mensaje.split('').map(char => char.charCodeAt(0).toString(2).padStart(8, '0')).join('');
}

// Función para agregar un error aleatorio en el mensaje binario
function introducirError(mensajeBinario) {
    const mensajeArray = mensajeBinario.split('');
    const bitDeError = Math.floor(Math.random() * mensajeBinario.length);
    mensajeArray[bitDeError] = mensajeArray[bitDeError] === '0' ? '1' : '0';  // Invertimos un bit al azar
    return mensajeArray.join('');
}

// Función para enviar el mensaje al servidor
function enviarMensaje(mensajeCodificado, conError, mensajeOriginal) {
    // Crear una nueva conexión al servidor
    const clientSocket = net.createConnection({ host: 'localhost', port: 12345 }, () => {
        console.log("Enviando mensaje codificado:", mensajeCodificado);
        // Si es con error, mostramos que es un mensaje con error
        console.log(conError ? "Enviando con error (con ruido)" : "Enviando sin error");
        clientSocket.write(mensajeCodificado); // Enviar el mensaje
    });

    // Recibir respuesta del servidor (mensaje decodificado)
    clientSocket.on('data', (data) => {
        const mensajeDecodificado = data.toString();
        console.log("Mensaje decodificado recibido:", mensajeDecodificado);
        // Guardar los resultados
        const mensajeResultado = (mensajeDecodificado === mensajeOriginal) ? "mensaje correcto" : "mensaje con error";
        
        // Determinar el archivo de resultados
        const tamanoMensaje = mensajeCodificado.length;
        const archivo = tamanoMensaje > 10000 ? 'resultados20k.txt' : 'resultados10k.txt';

        // Escribir el resultado en el archivo correspondiente
        const resultado = `${tamanoMensaje}, ${conError ? 0.01 : 0.0}, ${mensajeResultado}\n`;
        fs.appendFileSync(archivo, resultado);

        clientSocket.end();
    });

    clientSocket.on('error', (err) => {
        console.error("Error en el socket:", err.message);
    });
}

// Ejecutar pruebas automatizadas
pruebasAutomatizadas();
