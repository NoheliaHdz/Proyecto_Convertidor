# abcedario y sibolos especiales en el codigo morse
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
    morse_text = ''
    for char in text:
        morse_char = codigo_morse.get(char.upper(), None)
        if morse_char is not None:
            morse_text += morse_char + ' '
    return morse_text.strip()

# el usuarion ingresara e texto que desea codificar
text = input("Ingrese el texto que desea codificar: ")

# codificar texto en morse
codificar_texto = codificar_codigo(text)

# Inpresion del codigo morse
print("codigo morse:", codificar_texto)
