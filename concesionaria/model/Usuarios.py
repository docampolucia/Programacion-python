listaVehiculos = []
listaUsuarios = []

class Usuario():

    def __init__(self, nombre, apellido, mail, password):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.password = password
        self.agregarAlista()
   
    def agregarAlista(self):
        listaUsuarios.append(self)

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f'Nombre: {self.nombre}. Apellido: {self.apellido}. Correo: {self.mail}. Password: {self.password}.'
      
class UsuarioInvitado(Usuario):
    nivel = 'Invitado'

    def __str__(self):
        return f'Nombre: {self.nombre}. Apellido: {self.apellido}. Correo: {self.mail}. Password: {self.password}. NivelUsu: {self.nivel}.'

    def verLista(self):
        for vehiculo in listaVehiculos:
            print(f'Vehiculo:{vehiculo.marca}, Modelo: {vehiculo.modelo}, Detalles: {vehiculo.observaciones}')

class UsuarioEmpleado(UsuarioInvitado):
    nivel = 'Empleado'

    def verLista(self):
        for vehiculo in listaVehiculos:
            print(f'Vehiculo:{vehiculo.marca}, Modelo: {vehiculo.modelo}, Detalles: {vehiculo.observaciones}, Km:{vehiculo.km}, Precio:{vehiculo.precio}')
    
    def modificarPrecio(self, vehiculo, precioNuevo):
        if vehiculo in listaVehiculos:
            vehiculo.precio = precioNuevo
        else:
            print('El vehiculo no se encuentra en la lista')

    def modificarKm(self, vehiculo, KmNuevo):
        if vehiculo in listaVehiculos:
            vehiculo.km = KmNuevo
        else:
            print('El vehiculo no se encuentra en la lista')

    def modificarObservaciones(self, vehiculo, observacionesNuevas):
        if vehiculo in listaVehiculos:
            vehiculo.observaciones = observacionesNuevas
        else:
            print('El vehiculo no se encuentra en la lista')

    def agregarDetalle(self, vehiculo, detalleNuevo, valorNuevo):
        vehiculo.detalleNuevo = valorNuevo

class UsuarioAdmin(UsuarioEmpleado):
    nivel = 'Admin'

    def agregarUsuario(self, nombreUsuario, apellidoUsuario, mailUsuario, passwordUsuario, nivelUsuario):
        if nivelUsuario.lower() == 'invitado':
            nuevoUsuario = UsuarioInvitado(nombreUsuario, apellidoUsuario, mailUsuario, passwordUsuario)
            return nuevoUsuario
        elif nivelUsuario.lower() == 'empleado':
            nuevoUsuario = UsuarioEmpleado(nombreUsuario, apellidoUsuario, mailUsuario, passwordUsuario)
            return nuevoUsuario
        elif nivelUsuario.lower() == 'admin':
            nuevoUsuario = UsuarioAdmin(nombreUsuario, apellidoUsuario, mailUsuario, passwordUsuario)
            return nuevoUsuario
        else:
            print('El nivel de usuario ingresado es incorrecto')

    def agregarVehiculo(self, vehiculo):
        listaVehiculos.append(vehiculo)

