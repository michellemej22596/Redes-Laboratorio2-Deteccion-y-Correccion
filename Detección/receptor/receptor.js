const net = require('net');  // Requiere el módulo net para usar sockets
const { crc32_receptor } = require('./crc32');  // Importa la función para calcular CRC-32

const HOST = '127.0.0.1';  // Dirección IP (localhost)
const PORT = 65432;        // Puerto donde el emisor enviará los datos

// Crear el servidor de socket
const server = net.createServer((socket) => {
    console.log('Cliente conectado');

    // Evento para recibir los datos del cliente
    socket.on('data', (data) => {
        console.log('Datos recibidos del emisor');

        // Recibimos los datos enviados por el emisor (mensaje y CRC)
        let mensajeRecibido = data.toString(); // Convertimos los datos a cadena
        let [mensaje, crcRecibido] = mensajeRecibido.split('::'); // Dividimos el mensaje y CRC

        console.log(`Mensaje recibido: ${mensaje}`);
        console.log(`CRC recibido: ${crcRecibido}`);
        
        // Calculamos el CRC del mensaje recibido
        const crcCalculado = crc32_receptor(mensaje);
        console.log(`CRC calculado: ${crcCalculado}`);

        // Verificamos si el CRC calculado coincide con el CRC recibido
        if (crcCalculado === crcRecibido) {
            console.log('La integridad del mensaje es válida.');
            socket.write('La integridad del mensaje es válida.\n');
        } else {
            console.log('El mensaje ha sido corrompido.');
            socket.write('El mensaje ha sido corrompido.\n');
        }
    });

    // Evento para manejar errores
    socket.on('error', (err) => {
        console.log(`Error en la conexión: ${err.message}`);
    });

    // Evento cuando la conexión se cierra
    socket.on('end', () => {
        console.log('Cliente desconectado');
    });
});

// El servidor escucha en el puerto especificado
server.listen(PORT, HOST, () => {
    console.log(`Servidor de receptor escuchando en ${HOST}:${PORT}`);
});
