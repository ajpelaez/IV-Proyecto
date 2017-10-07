import blablacarapi
from blablacarapi import BlaBlaCarApi
from pocha import it, describe
import TripManager

@describe('TripManager tests')
def _():

    #Testea la funcion checkCity de la clase TripManager
    @it('Revisado que una ciudad existe.')
    def testCheckCity():
        tripManager = TripManager.TripManager()
        assert(True, tripManager.checkCity("Granada"))
        assert(False, tripManager.checkCity("Grandadada"))

    #Testea la funcion setTrips de la clase TripManager
    @it('Revisado que se introduce un origen y un destino válidos para el viaje.')
    def testSetTrips():
        tripManager = TripManager.TripManager()
        assert (1, tripManager.setTrips("",""))
        assert (2, tripManager.setTrips("Grandadada",""))
        assert (3, tripManager.setTrips("Granada","Grandadada"))
        assert (0, tripManager.setTrips("Granada","Madrid"))

    #Testea la funcion getTrips de la clase TripManager
    @it('Revisado que solo se devuelven viajes si hay viajes guardados.')
    def testGetTrips():
        tripManager = TripManager.TripManager()
        tripManager.trips = None
        assert (1, tripManager.getTrips())

        tripManager.setTrips("Granada","Madrid")
        api = BlaBlaCarApi(api_key="713d0cd3340f4e428c54177955de9f25", locale="es_ES", currency="es_ES")
        tipo = type(api.trips(frm="Granada", to="Madrid")).__name__
        tipo2 = type(tripManager.getTrips()).__name__
        assert (tipo, tipo2)
