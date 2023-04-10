class Camara:
    def __init__(self,id,nombre,resolucion) -> None:
        self.id = id
        self.nombre = nombre
        self.resolución = resolucion

    def transmitir(self):
        print("Iniciando transmision con dispositivo", self.nombre)