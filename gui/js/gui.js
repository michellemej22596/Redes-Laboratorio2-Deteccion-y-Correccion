document.getElementById('sendButton').addEventListener('click', function() {
  const message = document.getElementById('message').value;
  const algorithm = document.getElementById('algorithm').value;

  if (message.trim() === "") {
    alert("Por favor, ingresa un mensaje.");
    return;
  }

  // Enviar mensaje al socket
  sendToSocket(message, algorithm);
});

function sendToSocket(message, algorithm) {
  // Aquí se manejará la comunicación con los sockets (emisor-receptor)
  console.log(`Enviando mensaje: "${message}" usando el algoritmo: ${algorithm}`);
  // Llama a socket-gui.js para la comunicación
  sendMessageToReceiver(message, algorithm);
}
