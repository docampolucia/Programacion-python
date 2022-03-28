#Ejercicio 8 - Lucia Docampo
# Nombre y apellido
vocales = 0
while vocales < 3:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_completo = nombre + apellido
    vocales = 0
    for letra in nombre_completo.lower():
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales += 1

# Año de nacimiento
error = 1
while error > 0:
    año_de_nacimiento = input("Ingrese su año de nacimiento: ")
    error = 0
    while len(año_de_nacimiento) != 4:
        año_de_nacimiento = input("Ingrese su año de nacimiento: ")

    for caracter in año_de_nacimiento:
        if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
            continue
        else:
            error += 1

# Contraseña
carateres_especial = 0

while carateres_especial < 1:
    carateres_especial = 0
    contraseña = input("Ingrese una contraseña: ")  
    
    while len(contraseña) < 8 or len(contraseña) > 16:
        contraseña = input("Ingrese una contraseña: ")
    
    for caracter in contraseña:
        if caracter == "!" or caracter == '"' or caracter == "#" or caracter == "$" or caracter == "%" or caracter == "&":
            carateres_especial +=1 

print(f"¡Hola {nombre} {apellido}!")
