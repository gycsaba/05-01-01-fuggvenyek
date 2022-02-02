from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKor(TestCase):
    def test_teglalap_van(self):
        aktualis = feladatok.kor_terulet(5.3)
        elvart_sugar = 88.24733
        import math
        aktualis=math.isclose(aktualis, elvart_sugar, rel_tol=1e-4, abs_tol=0.0)
        elvart=True
        self.assertEqual(elvart, aktualis,"A kör területét legalább négy tizedes jegy pontossággal kell meghatározza! A képletbe ne használjon Ön által beírt konstans számot")

    def test_teglalap_van(self):
        aktualis = feladatok.kor_terulet(0)
        elvart=None
        self.assertEqual(elvart, aktualis,"A kör területét rosszul határozza meg, amikor a kör sugara nulla!")


    def test_teglalap_van(self):
        aktualis = feladatok.kor_terulet(-10)
        elvart=None
        self.assertEqual(elvart, aktualis,"A kör területét rosszul határozza meg, amikor a kör sugara negatív!")

