from model.Usuarios import *
from model.Vehiculos import *

elias = UsuarioAdmin('elias', 'prost', 'elias.prost@gmail.com', 'jajaja')

lucia = elias.agregarUsuario('lucia', 'docampo', 'lucia.docampo@gmail.com', 'jajaja', 'empleado')

luis = UsuarioInvitado('luis', 'nada','luis@gmail.co','jajaja')

auto1 = Auto('Renault', 'Clio', '17000', '')