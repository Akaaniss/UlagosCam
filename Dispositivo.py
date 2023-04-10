from Camara import Camara

class Dispositivo(Camara):
    def __init__(self,id,nombre,resolucion,marca,modelo) -> None:
        super().__init__(id,nombre,resolucion)
        self.marca = marca
        self.modelo = modelo