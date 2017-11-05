import blablacarapi
from blablacarapi import BlaBlaCarApi
from TripManager import TripManager
from blablacarapi import models
import unittest

class SimplisticTest(unittest.TestCase):

    def setUp(self):
        self.tripManager = TripManager()

    #Comprueba que si una ciudad existe, nuestra función dirá que existe
    def testCityExits(self):
        self.assertTrue(self.tripManager.checkCity("Granada") , "La ciudad Granada debería existir")

    #Comprueba que si una ciudad existe, nuestra función dirá que existe
    def testCityNoExits(self):
        self.assertFalse(self.tripManager.checkCity("Grandadada") , "La ciudad Grandadada no debería existir")

    #Comprueba que si intentamos guardar viajes con destino o origen erróneos, estos no se guarden
    #Y si guardamos viajes con destino y origen correctos, estos se guarden
    def testSetTrips(self):
        self.assertEqual(self.tripManager.setTrips("","Granada") , 1 , "No deberían guardarse viajes sin ciudad de salida")
        self.assertEqual(self.tripManager.setTrips("Grandadada","") , 2, "No deberían guardarse viajes con una ciudad de salida errónea")
        self.assertEqual(self.tripManager.setTrips("Granada","Grandadada") , 3, "No deberían guardarse viajes con una ciudad de destino errónea")
        self.assertEqual(self.tripManager.setTrips("Granada","Madrid") , 0, "Deberían de guardarse los viajes correctamente")

    #Comprueba que nuestra funcion getTrips solo nos devuelva viajes si tenemos viajes guardados
    def testGetTrips(self):
        self.tripManager.trips = None
        self.assertEqual(self.tripManager.getTrips(),1 ,"No debería haber viajes guardados")
        self.tripManager.setTrips("Granada","")
        viajes = (self.tripManager.getTrips())
        self.assertTrue("Granada" in viajes["viajes"][0]["departure_place"],
            "Debería haber por lo menos un viaje guardado")


if __name__ == '__main__':
    unittest.main()
