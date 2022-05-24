from model.Usuarios import *
from model.Vehiculos import *
from model.concesionaria import *
from model.prueba_usuarios import *

print("Bienvenido a la Concesionaria Lucia\nMenú de Opciones\n")
print("1. Registrar Nuevo usuario.\n2. Ingresar al Sistema con su usuario.\n3. Salir")    
op = 0
while op != 3:
    
    op = int(input("Ingrese la opcion que desea realizar: "))
    
    if op == 1:
        nombre = str(input("Ingrese su nombre: "))
        apellido = input("Ingrese su apellido: ")
        mail = input("Ingrese su mail: ")
        password = input("Ingrese su password: ")
        nivel = int(input("Ingrese:\n1 si es un usuario admin\n2 si es Empleado\n3 si es Invitado"))
        RegistrarUsuario(nombre, apellido, mail, password, nivel)
        break
    
    elif op == 2:
        mail = input("Ingrese su mail: ")
        password = input("Ingrese su password: ")
        buscarUsuario(mail, password)
        break

