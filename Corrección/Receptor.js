const net = require('net');

// Función para calcular la paridad
function calcularParidad(hammingCode, pos) {
    let paridad = 0;
    for (let i = 0; i < hammingCode.length; i++) {
        if ((i + 1) & pos) {  // Comprobamos si la posición i + 1 tiene un bit de paridad
            paridad ^= parseInt(hammingCode.charAt(i));  // XOR para obtener la paridad
        }
    }
    return paridad;
}

// Método para verificar y corregir el código Hamming
function corregirHamming(hammingCode) {
    let n = hammingCode.length;
    let errorPos = 0;

    for (let i = 0; (1 << i) <= n; i++) {
        let paridadPos = (1 << i);
        let paridad = calcularParidad(hammingCode, paridadPos);
        if (paridad !== 0) {
            errorPos += paridadPos;
        }
    }

    if (errorPos > 0) {
        console.log("Error en el bit: " + errorPos);
        let arr = hammingCode.split('');
        arr[errorPos - 1] = (arr[errorPos - 1] === '0') ? '1' : '0';
        hammingCode = arr.join('');
    } else {
        console.log("No se detectaron errores.");
    }

    return hammingCode;
}

// Función para decodificar el mensaje usando ASCII
function decodificarMensaje(mensajeCodificado) {
    let mensajeDecodificado = '';

    // Asegurarse de que el mensaje binario sea múltiplo de 8
    while (mensajeCodificado.length % 8 !== 0) {
        mensajeCodificado += '0';  // Rellenar con ceros al final
    }

    // Eliminar los bits de paridad (ubicados en las posiciones de 1, 2, 4, 8, ...)
    let mensajeSinParidad = '';
    let i = 0;

    // Eliminar los bits de paridad en las posiciones 1, 2, 4, 8, ...
    while (i < mensajeCodificado.length) {
        // Si la posición es una potencia de 2, es un bit de paridad
        if (Math.pow(2, Math.floor(Math.log2(i + 1))) === (i + 1)) {
            i++;
            continue;
        }

        mensajeSinParidad += mensajeCodificado.charAt(i);
        i++;
    }

    // Decodificar los 8 bits en caracteres ASCII
    for (let i = 0; i < mensajeSinParidad.length; i += 8) {
        const byte = mensajeSinParidad.substring(i, i + 8); 
        const charCode = parseInt(byte, 2);  
        mensajeDecodificado += String.fromCharCode(charCode); 
    }

    return mensajeDecodificado;
}

// Configurar servidor para recibir mensajes
const server = net.createServer((socket) => {
    console.log("Conexión establecida. Esperando mensaje...");

    socket.on('data', (data) => {
        const mensajeConRuido = data.toString();  // Asegurarse de recibir el mensaje correctamente como binario
        console.log("Mensaje recibido (con ruido):", mensajeConRuido);

        // Corregir errores en el mensaje recibido
        const mensajeCorregido = corregirHamming(mensajeConRuido);
        console.log("Mensaje recibido (con errores corregidos):", mensajeCorregido);

        // Decodificar el mensaje
        const mensajeDecodificado = decodificarMensaje(mensajeCorregido);
        console.log("Mensaje decodificado:", mensajeDecodificado);

        // Asegúrate de que la respuesta se envíe solo después de que el mensaje haya sido decodificado
        if (socket.writable) {
            socket.write(mensajeDecodificado, () => {
                console.log("Mensaje corregido y enviado de vuelta al emisor");
            });
        } else {
            console.error("Error: Socket no está escribible");
        }
    });

    socket.on('end', () => {
        console.log('Conexión cerrada');
    });

    socket.on('error', (err) => {
        console.error("Error en el socket:", err.message);
    });

    socket.on('close', () => {
        console.log('Conexión cerrada (por el servidor o cliente)');
    });
});

// Iniciar servidor
server.listen(12345, () => {
    console.log("Servidor escuchando en puerto 12345...");
});
