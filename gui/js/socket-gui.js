function sendMessageToReceiver(message, algorithm) {
  // Establecer la comunicación con el servidor a través del socket
  // Asegúrate de tener configurado el socket en el servidor
  console.log("Mensaje enviado: " + message);

  // Simulamos la verificación del mensaje con el CRC o Hamming
  // Aquí deberías integrar la lógica de los sockets reales que van del emisor al receptor
  setTimeout(() => {
    document.getElementById('status').textContent = `El mensaje fue enviado con el algoritmo: ${algorithm}`;
  }, 1000);
}
