from model.Usuarios import *
from model.Vehiculos import *

def buscarUsuario(mail, password):
    usuarioCorrecto = False
    for usuario in listaUsuarios:
        if usuario.mail == mail:
            if usuario.password == password:
                print('Inicio de sesión exitoso')
                usuarioCorrecto = True
            else:
                print('La contraseña es incorrecta')
    if usuarioCorrecto == False:
        print('El mail ingresado es incorrecto')

def RegistrarUsuario(nombre, apellido, mail, contraseña, nivel):
    if nivel == 1:
        usuario_ingresado = UsuarioInvitado(nombre, apellido, mail, contraseña)
        print(f'El usuario {nombre} ha sido registrado como Invitado')

    elif nivel == 2:
        usuario_ingresado = UsuarioEmpleado(nombre, apellido, mail, contraseña)
        print(f'El usuario {nombre} ha sido registrado como Empleado')

    elif nivel == 3:  			
        usuario_ingresado = UsuarioAdmin(nombre, apellido, mail, contraseña)
        print(f'El usuario {nombre} ha sido registrado como Administrador')

    else:
        print('El nivel de usuario ingresado no es válido, intente con 1, 2 o 3')

