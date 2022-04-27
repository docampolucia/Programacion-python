#Un concesionario te contrata para realizar un software ya que quiere llevar un
#control de los automóviles que tiene para vender. Se sabe que
#este concesionario vende: bicicletas, motos, autos, camioneta, colectivos, camiones y acoplados.
#Realizar las clases correspondientes a cada elemento. Generar objetos de cada una de las clases.
# Imprimir por terminal los ejemplos realizados con sus características.
# OPCIONAL: que el usuario ingrese los atributos de los objetos por consola.
# Para poder iniciar el software se debe ingresar con un usuario y contraseña. Deben existir tres perfiles de usuarios. 

#INVITADO:
#Solo puede ver el listado de los automóviles que tiene la concesionaria a la venta.
#Detalles de los vehículos.
#EMPLEADO:
#Puede ver los automóviles a la venta.
#Puede ver los precios y kilómetros del mismo.
#Puede modificar los kilómetros.
#Agregar detalles sobre el vehículo a la venta.
#ADMIN:
#Podes cargar nuevos automóviles.
#Cargar y modificar precio de los mismos.
#Puede modificar los kilómetros.
#Crear nuevos usuarios invitados y usuarios standard.
#Agregar detalles sobre el vehículo a la venta.

class Bicicletas:
    def __init__(self, color, rodado):
    self.color = color
    self.rodado = rodado

class Motos:
    def __init__(self, color, marca):
    self.color = color
    self.marca = marca

class Autos:
    def __init__(self, color, marca):
    self.color = color
    self.marca = marca

class Camioneta:
    def __init__(self, color, marca):
    self.color = color 
    self.marca = marca

class Colectivos:
   def __init__(self, color, marca):
    self.color = color
    self.marca = marca

class Camiones:
    def __init__(self, color, marca):
    self.color = color 
    self.marca = marca

class Acoplados:
    def __init__(self, color, marca):
    self.color = "" 
    self.marca = ""

bici1 = Bicicletas (color, rodadobici1)

bici1 = input("Ingrese el color de su bicicleta: ")

Bicicletas.rodado = input("Ingrese el rodado de su bicicleta: ")
print(f"Su bicicleta es de color ", Bicicletas.color, "y tiene rodado ",Bicicletas.rodado,".")

Motos.color = input("Ingrese el color de su moto: ")
Motos.marca = input("Ingrese la marca de su moto: ")
print(f"Su bicicleta es de color ", Motos.color, "y tiene rodado ",Motos.marca,".")

autos.color = input("Ingrese el color de su auto: ")
autos.marca = input("Ingrese la marca de su auto: ")
autos.modelo = input("Ingrese el modelo de su auto: ")
print(f"Su auto es un ", autos.marca,autos.modelo, "de color ",autos.color,".")

bicicletas.color = input("Ingrese el color de su bicicleta: ")
bicicletas.rodado = input("Ingrese el rodado de su bicicleta: ")
print(f"Su bicicleta es de color ", bicicletas.color, "y tiene rodado ",bicicletas.rodado,".")

