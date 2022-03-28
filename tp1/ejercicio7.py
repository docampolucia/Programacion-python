#Ejercicio 7 - Lucia Docampo
nombre = input("Ingrese su nombre: ")
edad = int (input("Ingrese su edad: "))
dinero = float (input("Ingrese el dinero que tiene en su billetera: "))
hambre = int (input("Ingrese el hambre que tiene (0-10): "))

if edad < 35:
    print(f"Hola {nombre}. Eres una persona joven ya que tu edad es {edad}.")

if edad > 34 and dinero > 500 and hambre > 5:
    print(f"Hola {nombre}, ¿Hoy hay asado?")

if (hambre > 6 or dinero < 100) and edad < 18:
    print(f"Hola {nombre}, ¿vas a comer a lo de tus padres?")