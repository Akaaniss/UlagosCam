from Dispositivo import Dispositivo
from Sesion import Sesion

class Main:
    def __init__(self) -> None:
        self.sesion = Sesion(0,"","","","","","",Dispositivo(0,"",0,"",""),[])
        tecla = -1;

        while(tecla != 0):
            print("--- Bienvenid@ a U Lagos Cam---")
            print("Ingrese una opción:")
            print("")
            print("0) Salir.")
            print("1) Crear Sesión.")
            print("2) Cambiar Camara.")
            tecla = int(input("Ingrese una opción: "))

            if(tecla == 0):
                print("Saliendo del programa")
            if(tecla == 1):
                self.generarSesion()
            if(tecla == 2):
                self.cambiarCamara()

    def generarSesion(self):
        listaCamaras = []
        print("--- Generando sesión ---")
        idSesion = int(input("Ingrese id sesion: "))
        asignatura = input("Ingrese asignatura: ")
        profesor = input("Ingrese profesor: ")
        sala = input("Ingrese sala: ")
        fecha = input("Ingrese fecha: ")
        horaInicio = input("Ingrese hora inicio: ")
        horaFin = input("Ingrese hora fin: ")
        cantidadCamaras = int(input("Ingrese cantidad de cámaras: "))
        camaraEnUso = Dispositivo(0,"",0,"","")

        for i in range (0,cantidadCamaras):
            print("--- Ingresando camara ---")
            idCamara = int(input("Ingrese id camara: "))
            nombre = input("Ingrese nombre: ")
            resolucion = int(input("Ingrese resolucion: "))
            marca = input("Ingrese marca: ")
            modelo = input("Ingrese modelo: ")

            dispositivo = Dispositivo(idCamara,nombre,resolucion,marca,modelo)

            listaCamaras.append(dispositivo)

        self.sesion = Sesion(idSesion,asignatura,profesor,sala,fecha,horaInicio,horaFin,listaCamaras[0],listaCamaras)
        self.sesion.iniciarTransmision()

    def cambiarCamara(self):
        if(len(self.sesion.lista_camaras) > 0):
            print("Cambiando Camara")
            self.sesion.cambiarCamara()
            self.sesion.camara_en_uso.transmitir()
        else:
            print("No se ha generado ninguna sesión todavía.")

main = Main()