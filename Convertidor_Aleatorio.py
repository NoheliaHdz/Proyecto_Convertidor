
import random


def decimal_a_romano(num_decimal):
    """
    Convertir de decimal a numeros romanos.
    """
    mapa_numeros_romanos = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                         ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                         ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    numero_romano = ''
    while num_decimal > 0:
        for numeros, value in mapa_numeros_romanos:
            while num_decimal >= value:
                numero_romano += numeros
                num_decimal -= value
    return numero_romano
# llamado de la funcion definida anteriormente
#numero_romano = decimal_a_romano(num_decimal)

codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' '
}

def codificar_codigo(text):
    """
    Convertir texto a codigo morse.
    """
    morse_text = ''
    for char in text:
        morse_char = codigo_morse.get(char.upper(), None)
        if morse_char is not None:
            morse_text += morse_char + ' '
    return morse_text.strip()


# codificar texto en morse
#codificar_texto = codificar_codigo(text)

# Inpresion del codigo morse
#print("codigo morse:", codificar_texto)


def decimal_a_binario(num_decimal):
    """
    Convertir de decimal a binario.
    """
    num_binario = bin(num_decimal)
    return num_binario

def decimal_a_hexa(num_decimal):
    """
    Convertir de decimal a hexadecimal.
    """
    num_hexa = hex(num_decimal)
    return num_hexa

def decimal_a_octa(num_decimal):
    """
    Convertir de decimal a octal.
    """
    num_octal = oct(num_decimal)
    return num_octal


# peticion del numero al usuario
num_decimal = int(input("Ingrese el numero que desea convertir "))

# variable funcion que se encargara de dar la funcion aleatorea 
funcion_conversion = random.choice([decimal_a_binario, decimal_a_hexa, decimal_a_octa, decimal_a_romano, codificar_codigo])


resultado = funcion_conversion(num_decimal)

# Imprimir resultado
print(f"La {funcion_conversion.__name__.replace('_', ' ')} es la representacion {num_decimal} es: {resultado}")

