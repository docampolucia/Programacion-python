#Ejercicio 10 - Lucia Docampo
import random
numeros = [1,2,3,4,5,6,7,8,9,10] 
intentos_restantes = 5

for i in range(5): 
    numero_elegido = int(input("Elija un numero entero del 1 al 10: "))
    numero_sorteado = random.choice(numeros)
    intentos_restantes -= 1

    if numero_elegido == numero_sorteado:
        print("¡Ganaste!")
        break
    else:
        print(f"Te quedan {intentos_restantes} intentos, el número sorteando fue: {numero_sorteado}.")

 