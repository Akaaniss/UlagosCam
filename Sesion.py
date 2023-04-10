class Sesion:
 def __init__(self,id,asignatura,profesor,sala,fecha,hora_inicio,hora_fin,camara_en_uso,lista_camaras) -> None:
  self.id = id
  self.asignatura = asignatura
  self.profesor = profesor
  self.sala = sala
  self.fecha = fecha
  self.hora_inicio = hora_inicio
  self.hora_fin =hora_fin
  self.camara_en_uso = camara_en_uso
  self.lista_camaras = lista_camaras

 def iniciarTransmision(self):
  print("Comenzando Transmisión")
  self.camara_en_uso.transmitir()

 def terminarTransmision(self):
  print("Terminando transmision")

 def cambiarCamara(self):
  largoArray = len(self.lista_camaras)
  indiceSeleccionado = 0
  for i in range (0,largoArray):
   if(self.camara_en_uso.id == self.lista_camaras[i].id):
    indiceSeleccionado = i
  if(indiceSeleccionado == largoArray-1):
   self.camara_en_uso = self.lista_camaras[0]
  else:
   self.camara_en_uso = self.lista_camaras[indiceSeleccionado+1]