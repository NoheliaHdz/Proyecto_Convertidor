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
# Ingreso de los usuarios
num_decimal = int(input("Ingresa el numero decimal: ")) 

# llamado de la funcion definida anteriormente
numero_romano = decimal_a_romano(num_decimal)

print(f"La representacion romana de {num_decimal} es: {numero_romano}")
