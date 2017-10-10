import blablacarapi
from blablacarapi import BlaBlaCarApi
from pocha import it, describe
import TripManager
from blablacarapi import models

@describe('TripManager tests')
def _():

    #Testea la funcion checkCity de la clase TripManager
    @it('Revisado que una ciudad existe.')
    def testCheckCity():
        tripManager = TripManager.TripManager()
        assert tripManager.checkCity("Granada") is True , "La ciudad de origen no existe"
        assert tripManager.checkCity("Grandadada") is False, "La ciudad de origen no existe"

    #Testea la funcion setTrips de la clase TripManager
    @it('Revisado que se introduce un origen y un destino válidos para el viaje.')
    def testSetTrips():
        tripManager = TripManager.TripManager()
        assert tripManager.setTrips("","") == 1 , "El viaje debe tener un destino y origen válidos"
        assert tripManager.setTrips("Grandadada","") == 2, "El viaje debe tener un destino y origen válidos"
        assert tripManager.setTrips("Granada","Grandadada") == 3, "El viaje debe tener un destino y origen válidos"
        assert tripManager.setTrips("Granada","Madrid") == 0, "El viaje debe tener un destino y origen válidos"

    #Testea la funcion getTrips de la clase TripManager
    @it('Revisado que solo se devuelven viajes si hay viajes guardados.')
    def testGetTrips():
        tripManager = TripManager.TripManager()
        tripManager.trips = None
        assert tripManager.getTrips() == 1, "No hay viajes guardados"
        tripManager.setTrips("Granada","Madrid")
        assert type(tripManager.getTrips()) is models.Trips, "No hay viajes guardados"
