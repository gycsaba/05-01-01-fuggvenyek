from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestNagyobb(TestCase):
    def test_nagyobb_elso(self):
        aktualis = feladatok.nagyobb(5,3)
        elvart = 5
        self.assertEqual(elvart, aktualis, "nagyobb(5,3) visszatérési értéke nem 5")

    def test_nagyobb_masodik(self):
        aktualis = feladatok.nagyobb(3,5)
        elvart = 5
        self.assertEqual(elvart, aktualis, "nagyobb(3,5) visszatérési értéke nem 5")

    def egyenloek(self):
        aktualis = feladatok.nagyobb(5,5)
        elvart = 5
        self.assertEqual(elvart, aktualis, "nagyobb(5,5) visszatérési értéke nem 5")
