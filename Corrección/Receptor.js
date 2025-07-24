// Método para calcular la paridad
function calcularParidad(hammingCode, pos) {
    let paridad = 0;
    for (let i = 0; i < hammingCode.length; i++) {
        if ((i + 1) & pos) {  // Comprobamos si la posición i + 1 tiene un bit de paridad
            paridad ^= parseInt(hammingCode.charAt(i));  // XOR para obtener la paridad
        }
    }
    return paridad;
}

// Método para generar el código Hamming
function generarCodigoHamming(datos) {
    datos = datos.split('');
    
    // Calcular la cantidad de bits de paridad necesarios
    let n = datos.length;
    let m = 0;
    while (Math.pow(2, m) < (n + m + 1)) {
        m++;
    }
    
    // Inserta los bits de paridad
    let hammingCode = new Array(n + m).fill('');
    let j = 0;
    for (let i = 1; i <= n + m; i++) {
        if ((i & (i - 1)) === 0) {  // Si es una posición de bit de paridad
            hammingCode[i - 1] = '0';
        } else {
            hammingCode[i - 1] = datos[j++];
        }
    }
    
    // Asignar los valores a los bits de paridad
    for (let i = 0; i < m; i++) {
        let paridadPos = Math.pow(2, i);
        let paridadBit = calcularParidad(hammingCode.join(''), paridadPos);  // Cambié aquí para que sea una cadena
        hammingCode[paridadPos - 1] = paridadBit;
    }

    return hammingCode.join('');  // Devolvemos como una cadena
}

// Método para verificar y corregir el código Hamming
function corregirHamming(hammingCode) {
    let n = hammingCode.length;
    let errorPos = 0;

    // Verifica los bits de paridad
    for (let i = 0; (1 << i) <= n; i++) {
        let paridadPos = (1 << i);
        let paridad = calcularParidad(hammingCode, paridadPos);
        if (paridad !== 0) {
            errorPos += paridadPos;  // Si hay un error, se calcula la posición
        }
    }

    // Si se detecta un error, corregir el bit erróneo
    if (errorPos > 0) {
        console.log("Error en el bit: " + errorPos);
        let arr = hammingCode.split('');  // Convertimos la cadena en un arreglo para modificar un carácter
        arr[errorPos - 1] = (arr[errorPos - 1] === '0') ? '1' : '0';  // Corregimos el bit
        hammingCode = arr.join('');  // Convertimos el arreglo nuevamente en una cadena
    } else {
        console.log("No se detectaron errores.");
    }

    return hammingCode;
}

// Método para verificar y corregir el código Hamming
function corregirHamming(hammingCode) {
    let n = hammingCode.length;
    let errorPos = 0;

    // Verifica los bits de paridad
    for (let i = 0; (1 << i) <= n; i++) {
        let paridadPos = (1 << i);
        let paridad = calcularParidad(hammingCode, paridadPos);
        if (paridad !== 0) {
            errorPos += paridadPos;  // Si hay un error, se calcula la posición
        }
    }

    // Si se detecta un error, corregir el bit erróneo
    if (errorPos > 0) {
        console.log("Error en el bit: " + errorPos);
        let arr = hammingCode.split('');  // Convertimos la cadena en un arreglo para modificar un carácter
        arr[errorPos - 1] = (arr[errorPos - 1] === '0') ? '1' : '0';  // Corregimos el bit
        hammingCode = arr.join('');  // Convertimos el arreglo nuevamente en una cadena
    } else {
        console.log("No se detectaron errores.");
    }

    return hammingCode;
}

// Función para modificar al menos dos bits del mensaje
function modificarBits(mensaje, numErrores) {
    let mensajeModificado = mensaje.split('');
    
    for (let i = 0; i < numErrores; i++) {
        const randomIndex = Math.floor(Math.random() * mensajeModificado.length); // Generar un índice aleatorio
        mensajeModificado[randomIndex] = (mensajeModificado[randomIndex] === '0') ? '1' : '0';  // Cambiar el bit
    }

    return mensajeModificado.join('');
}

// Función para verificar si el mensaje tiene errores y corregirlo
function verificarYCorregir(mensajeConError) {
    // Verifica y corrige errores utilizando el código Hamming actual
    let mensajeCorregido = corregirHamming(mensajeConError);
    
    // Si el mensaje corregido es igual al mensaje original, entonces no hubo error
    return mensajeCorregido;
}

// Pruebas con mensajes de diferentes longitudes
const mensajes = ["101010", "11011011", "1111001001"];
mensajes.forEach(mensaje => {
    // Emisor genera el código Hamming
    const codigo_hamming = generarCodigoHamming(mensaje);
    console.log("Código Hamming generado: ", codigo_hamming);

    // Modificar dos bits del código para simular errores
    let codigo_con_error = modificarBits(codigo_hamming, 2);  // Introducimos 2 errores
    console.log("Código con errores: ", codigo_con_error);

    // Receptor recibe el código Hamming con error y lo corrige
    const codigo_recibido = verificarYCorregir(codigo_con_error);
    console.log("Código recibido (con errores corregidos): ", codigo_recibido);

    // Comprobamos que el código recibido después de la corrección sea igual al código original
    if (codigo_recibido === codigo_hamming) {
        console.log("El código ha sido corregido correctamente.");
    } else {
        console.log("Se ha detectado un error, el mensaje se descarta.");
    }
});

// Ejemplo de uso
let hammingCode = "1011011001";  // Suponiendo que esta es la entrada con el código Hamming recibido
let codigoCorregido = corregirHamming(hammingCode);
console.log("Código corregido: " + codigoCorregido);

module.exports = { 
    generarCodigoHamming, 
    corregirHamming, 
    modificarBits, 
    verificarYCorregir 
};