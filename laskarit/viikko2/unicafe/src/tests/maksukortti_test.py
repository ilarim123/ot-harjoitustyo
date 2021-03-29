import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.12")
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")
        self.maksukortti.ota_rahaa(9)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")
        self.assertEqual(self.maksukortti.ota_rahaa(3), True)
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)

