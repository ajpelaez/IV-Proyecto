import blablacarapi
from blablacarapi import BlaBlaCarApi
import TripManager
import unittest


class SimplisticTest(unittest.TestCase):

    #Testea la funcion checkCity de la clase TripManager
    def testCheckCity(self):
        self.tripManager = TripManager.TripManager()
        self.assertTrue(self.tripManager.checkCity("Granada"))
        self.assertFalse(self.tripManager.checkCity("Grandadada"))

    #Testea la funcion setTrips de la clase TripManager
    def testSetTrips(self):
        self.tripManager = TripManager.TripManager()
        self.assertEqual(1, self.tripManager.setTrips("",""))
        self.assertEqual(2, self.tripManager.setTrips("Grandadada",""))
        self.assertEqual(3, self.tripManager.setTrips("Granada","Grandadada"))
        self.assertEqual(0, self.tripManager.setTrips("Granada","Madrid"))

    #Testea la funcion getTrips de la clase TripManager
    def testGetTrips(self):
        self.tripManager = TripManager.TripManager()
        self.assertEqual(1, self.tripManager.getTrips())
        
        self.tripManager.setTrips("Granada","Madrid")
        api = BlaBlaCarApi(api_key="713d0cd3340f4e428c54177955de9f25", locale="es_ES", currency="es_ES")
        tipo = type(api.trips(frm="Granada", to="Madrid")).__name__
        tipo2 = type(self.tripManager.getTrips()).__name__
        self.assertEqual(tipo, tipo2)


if __name__ == '__main__':
    unittest.main()
