#Ejercicio 6 - Lucia Docampo
nombres = []
rta = input("Ingrese el nombre de un amigue, caso contrario tipear exit para salir: ")

while rta != "exit":
    nombres.append(rta)
    rta = input("Ingrese el nombre de otro amigue, caso contrario tipear exit para salir: ")

if len(nombres) > 0:
    print("Los nombres de tus amigues son:", ", ".join(nombres))
