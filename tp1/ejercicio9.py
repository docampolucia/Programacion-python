# Ejercicio 9 - Lucia Docampo
# Chequear si ambos caracteres son números
error_1 = 1
while error_1 > 0:
    error_1 = 0
    numero_1 = input("Ingrese el primer número de la operación: ")
    for caracter in numero_1:
            if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
                continue
            else:
                error_1 += 1

error_2 = 1
while error_2 > 0:
    error_2 = 0
    numero_2 = input("Ingrese el segundo número de la operación: ")
    for caracter in numero_2:
            if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
                continue
            else:
                error_2 += 1

# Definir operacion
operacion = input("Seleccione una operación (+, -, *, /): ")
numero_1 = float(numero_1)
numero_2 = float(numero_2)

if operacion == "+":
    print(numero_1 + numero_2)

if operacion == "-":
    print(numero_1 - numero_2)

if operacion == "*":
    print(numero_1 * numero_2)

if operacion == "/":
    print(numero_1 / numero_2)