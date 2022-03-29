#Ejercicio 1 - Lucia Docampo
materias = []
for i in range(4) :
        opcion = input("\n ¿Qué materia estás cursando este año? \n Ingresa el nombre de una de ellas: ")
        materias.append(opcion)
        nota1=float (input("Ingrese la nota del primer parcial: ") )
        nota2=float (input("Ingrese la nota del segundo parcial: ") )
        nota3=float (input("Ingrese la nota del tercer parcial: ") )
        sumanotas= (nota1 + nota2 + nota3)
        promedionotas= sumanotas/3
        print(f"El promedio de la materia es {promedionotas}")

        if promedionotas >= 8 :
                print("La materia esta promocionada.")
        elif promedionotas >= 6 :
                print("La materia esta aprobada.")
        else:
                print ("La materia esta desaprobada.")

rta = input("Desea ingresar otra materia? (si/no)")
while rta.lower() != "no":
        opcion = input("\n ¿Qué materia estás cursando este año? \n Ingresa el nombre de una de ellas: ")
        materias.append(opcion)
        nota1=float (input("Ingrese la nota del primer parcial: ") )
        nota2=float (input("Ingrese la nota del segundo parcial: ") )
        nota3=float (input("Ingrese la nota del tercer parcial: ") )
        sumanotas= (nota1 + nota2 + nota3)
        promedionotas= sumanotas/3
        print(f"El promedio de la materia es {promedionotas}")

        if promedionotas >= 8 :
                print("La materia esta promocionada.")
        elif promedionotas >= 6 :
                print("La materia esta aprobada.")
        else:
                print ("La materia esta desaprobada.")

        rta = input("Desea ingresar otra materia? (si/no): ")
        
print( f"Las materias que cursa este año son: {materias}")
