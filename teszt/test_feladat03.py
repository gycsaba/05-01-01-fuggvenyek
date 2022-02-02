from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTeglalap(TestCase):
    def test_teglalap_van(self):
        aktualis = feladatok.teglalap_terulet(5.3,7.4)
        elvart = 39.22
        self.assertEqual(elvart, aktualis, "A teglalap_terulet üggvény létező téglalap területét nem jól határozza meg!")

    def test_teglalap_nincs_1(self):
        aktualis = feladatok.teglalap_terulet(0, 7.4)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha az egyik oldal nulla, a teglalap_terulet függvény nem jól határozza meg az értéket")

    def test_teglalap_nincs_2(self):
        aktualis = feladatok.teglalap_terulet(5, 0)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha az egyik oldal nulla, a teglalap_terulet függvény nem jól határozza meg az értéket")

    def test_teglalap_nincs_3(self):
        aktualis = feladatok.teglalap_terulet(0, 0)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha mindkét oldal nulla, a teglalap_terulet függvény nem jól határozza meg az értéket")


    def test_teglalap_negativ_1(self):
        aktualis = feladatok.teglalap_terulet(-1, 7.4)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha az egyik oldal negatív, a teglalap_terulet függvény nem jól határozza meg az értéket")

    def test_teglalap_negativ_2(self):
        aktualis = feladatok.teglalap_terulet(5, -1)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha az egyik oldal negatív, a teglalap_terulet függvény nem jól határozza meg az értéket")

    def test_teglalap_negativ_3(self):
        aktualis = feladatok.teglalap_terulet(-2, -1)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha mindkét oldal negítív, a teglalap_terulet függvény nem jól határozza meg az értéket")



