from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_osszeg(self):
        aktualis = feladatok.osszeg(5,3)
        elvart = 8
        self.assertEqual(elvart, aktualis, "A függvény két egész számot nem megfelelően ad össze!")
    def test_osszeg_negativ(self):
        aktualis = feladatok.osszeg(-5,-3)
        elvart = -8
        self.assertEqual(elvart, aktualis, "A függvény két negativ egész számot nem megfelelően ad össze!")
    def test_osszeg_poz_es_neg(self):
        aktualis = feladatok.osszeg(-5,3)
        elvart = -2
        self.assertEqual(elvart, aktualis, "A függvény egy negatív és egy pozitív számot nem megfelelően ad össze!")


