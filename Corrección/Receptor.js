// Método para calcular la paridad
function calcularParidad(hammingCode, pos) {
    let paridad = 0;
    for (let i = 0; i < hammingCode.length; i++) {
        if ((i + 1) & pos) {  // Comprobamos si la posición i + 1 tiene un bit de paridad
            paridad ^= parseInt(hammingCode.charAt(i));  // charAt ahora funciona si hammingCode es una cadena
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
        let arr = hammingCode.split('');  // Convertimos la cadena en un arreglo para modificar un carácter
        arr[errorPos - 1] = (arr[errorPos - 1] === '0') ? '1' : '0';  // Corregimos el bit
        hammingCode = arr.join('');  // Convertimos el arreglo nuevamente en una cadena
    }

    return hammingCode;
}

module.exports = { generarCodigoHamming, corregirHamming };  // Exportar las funciones
