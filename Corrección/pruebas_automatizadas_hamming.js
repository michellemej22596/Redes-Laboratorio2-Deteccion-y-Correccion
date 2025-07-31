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

    // Realizar las pruebas
    mensajesPrueba.forEach(mensaje => {
        // 1. Generar prueba sin error
        const mensajeBinario = convertirAMensajeBinario(mensaje);
        console.log(`\nProbando con mensaje sin error: "${mensaje}"`);
        console.log("Mensaje binario:", mensajeBinario);
        enviarMensaje(mensajeBinario, false); // Sin error

        // 2. Generar prueba con error (introducimos un error en 1 bit)
        const mensajeConError = introducirError(mensajeBinario);
        console.log(`\nProbando con mensaje con error: "${mensaje}"`);
        console.log("Mensaje binario con error:", mensajeConError);
        enviarMensaje(mensajeConError, true); // Con error
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
function enviarMensaje(mensajeCodificado, conError) {
    // Crear una nueva conexión al servidor
    const clientSocket = net.createConnection({ host: 'localhost', port: 12345 }, () => {
        console.log("Enviando mensaje codificado:", mensajeCodificado);
        // Si es con error, mostramos que es un mensaje con error
        console.log(conError ? "Enviando con error (con ruido)" : "Enviando sin error");
        clientSocket.write(mensajeCodificado); // Enviar el mensaje
    });

    // Recibir respuesta del servidor (mensaje decodificado)
    clientSocket.on('data', (data) => {
        console.log("Mensaje decodificado recibido:", data.toString());
        clientSocket.end();
    });

    clientSocket.on('error', (err) => {
        console.error("Error en el socket:", err.message);
    });
}

// Ejecutar pruebas automatizadas
pruebasAutomatizadas();
