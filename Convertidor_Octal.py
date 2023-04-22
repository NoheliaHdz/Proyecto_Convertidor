#Ingresa el usuario
num_decimal = int(input("Ingrese el numero decimal: "))  

# use the built-in oct() function to convert the decimal number to octal
num_octal = oct(num_decimal)

print(f"La representacion octal de {num_decimal} es: {num_octal}")