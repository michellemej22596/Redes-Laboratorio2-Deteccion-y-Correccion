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

// Ejemplo de uso
let hammingCode = "1011011001";  // Suponiendo que esta es la entrada con el código Hamming recibido
let codigoCorregido = corregirHamming(hammingCode);
console.log("Código corregido: " + codigoCorregido);
