import numpy as np

filas = 5 
columnas = 5
arreglo_vacio = np.zeros([filas,columnas])
barcos = np.array([[1,1,1,0,0],
                    [0,0,0,0,1],
                    [1,0,1,0,0],
                    [1,0,1,0,0],
                    [1,0,1,0,0]])

print("--------Batalla Naval-------\n Los barcos se encuentran en una matriz de 5 filas y 5 columnas.")
print("\nPara ganar es necesario que encuentres los barcos, tenes 4 intentos para hacerlo \nQUE COMIENCE EL JUEGO:")
x= 0
vidas= 4
arreglo_vacio = barcos
while vidas > 0: 
    try:      
        fila= int(input("Indique la fila donde cree que se encuentra el barco: "))
        columna= int(input("Indique columna donde cree que se encuentra el barco: ")) 
    except ValueError:
        print("Recorda que el numero de la fila y columna deben ser numeros entre el 1 y el 5.")
    except :
        print("Recorda que el numero de la fila y columna deben ser numeros entre el 1 y el 5.")
    else:
        if barcos[fila-1,columna-1] and arreglo_vacio[fila-1,columna-1]:
            print("Me diste :(")
            arreglo_vacio[fila-1,columna-1]=0
            x +=1
        else:
            print(f"Casi, no hay nada!")
            vidas -= 1
            print(f"Segui participando. Te quedan {vidas} intentos.")
        if x == 9:
            vidas = 0

if vidas == 0 and x == 9:
    print("GANASTE \U0001F973")

print("Los barcos estaban ubicados de ésta forma:")
print(barcos)