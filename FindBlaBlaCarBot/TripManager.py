from blablacarapi import BlaBlaCarApi
import requests

class TripManager:
    def __init__(self):
        #Inicio de la API con nuestra API Key
        self.api = BlaBlaCarApi(api_key="713d0cd3340f4e428c54177955de9f25", locale="es_ES", currency="es_ES")
        self.trips = None
    
    #checkCity nos dirá si una ciudad existe o no consultando la web de eltiempo.es
    def checkCity(self,city):
        #Reemplazamos espacios por - para que el nombre sea válido para la URL
        city = city.replace(" ", "-")
        r = requests.get("https://www.eltiempo.es/"+city+".html")
        if(r.status_code == 404):
            return False
        else:
            return True

    #setTrips guarda los viajes disponibles
    def setTrips(self,src,dest=""):
        if (src==""):
            return 1 #No se ha seleccionado ciudad de salida
        elif not self.checkCity(src):
            return 2 #La ciudad de origen no existe
        elif dest!="" and not self.checkCity(dest):
            return 3 #La ciudad de destino no existe
        else:
            self.trips = self.api.trips(frm=src, to=dest)
            return 0 #Todo correcto viajes guardados

    #getTrips te devuelve los viajes guardados
    def getTrips(self):
        if self.trips == None:
            return 1    #No hay viajes
        else:
            return self.trips
