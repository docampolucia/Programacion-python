import numpy as np 

#Batalla naval de 10 x 10
print(" ----- Batalla naval ------ \n Tenes 3 intentos para acertar donde estan los barcos:")

def batallanaval(i=0,j=0):
    for i in range(1,11):     # 10 filas
        for j in range(1,11): # 10 columnas
            if i == 1 and (j == 6 or j == 7 or j == 8 or j == 9 or j == 10):
                print(1, end = " ")
            elif i == 2 and (j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
                print(1, end = " ")
            elif i == 4 and (j == 3 or j == 4 or j == 5 or j == 6):
                print(1, end = " ")
            elif i == 5 and j == 1:
                print(1, end = " ")
            elif i == 6 and j== 1:
                print (1, end = " ")
            elif i == 7 and j == 1:
                print(1, end = " ")
            elif i == 6 and j== 5:
                print (1, end = " ")
            elif i == 7 and j == 5:
                print(1, end = " ")
            elif i == 8 and j== 5:
                print (1, end = " ")
            elif i == 9 and j == 5:
                print(1, end = " ")
            elif i == 10 and j== 5:
                print (1, end = " ")
            elif i == 10 and j== 8:
                print (1, end = " ")
            elif i == 6 and j == 8:
                print(1, end = " ")
            elif i == 7 and j== 8:
                print (1, end = " ")
            elif i == 8 and j == 8:
                print(1, end = " ")
            elif i == 9 and j== 8:
                print (1, end = " ")
            else:
                print (0, end = " ")
        print("\n")

vida= 0
while vida < 4: 
    vida += 1
    intento_i= int(input("Indique la fila donde cree que se encuentra el barco: "))
    intento_j = int(input("Indique columna donde cree que se encuentra el barco: ")) 
    bomba = [intento_i,intento_j]
    if intento_i == 1 and intento_j == 1:
        print("Hundiste el barco!")
        break
    else:
        print(f"Segui participando. Te quedan {vida} intentos.")
