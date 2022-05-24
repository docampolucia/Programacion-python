class Vehiculo:
    def __init__(self, marca, modelo, km, precio, observaciones):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.precio= precio
        self.observaciones = observaciones
    
    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.observaciones}'

class Auto(Vehiculo):
    pass

class Moto(Vehiculo):
    pass
    
class Camioneta(Vehiculo): 
    pass

class Camiones(Vehiculo):
    pass

class Acoplados(Vehiculo):
    pass

class Colectivos(Vehiculo):
    pass

class Bicicletas:
    def __init__(self, marca, rodado, color, precio, observaciones):
        self.marca = marca
        self.rodado = rodado
        self.color = color
        self.precio= precio
        self.observaciones = observaciones
    
    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.observaciones}'