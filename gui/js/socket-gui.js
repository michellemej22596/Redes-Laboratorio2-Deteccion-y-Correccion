const net = require('net');

// Configuración del socket para enviar datos al receptor
function sendMessageToReceiver(message, algorithm) {
  const client = new net.Socket();

  client.connect(65432, '127.0.0.1', () => {
    console.log('Conectado al receptor');

    // Enviar el mensaje con el CRC al receptor
    const crc = calculateCRC(message, algorithm);  // Calcula el CRC para el mensaje
    const messageWithCRC = `${message}::${crc}`;  // Formato: mensaje::CRC
    client.write(messageWithCRC);

    // Recibir la respuesta del receptor
    client.on('data', (data) => {
      console.log('Respuesta del receptor: ' + data.toString());
      document.getElementById('status').textContent = data.toString();
      client.destroy();  // Cierra la conexión
    });
  });

  client.on('error', (err) => {
    console.log('Error: ' + err.message);
  });

  client.on('close', () => {
    console.log('Conexión cerrada');
  });
}

// Función para calcular CRC-32 (similar a lo que ya tienes en crc32.js)
function calculateCRC(message, algorithm) {
  if (algorithm === "crc32") {
    // Aquí deberías utilizar el código de CRC-32 que ya tienes en crc32.js
    return crc32(message);  // Suponiendo que crc32 es la función que calcula el CRC-32
  }
  return "Algoritmo no soportado";
}
