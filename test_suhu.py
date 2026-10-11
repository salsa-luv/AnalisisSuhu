import unittest
from analisis_suhu import hitung_rata_rata, analisis_suhu

class TestSuhu(unittest.TestCase):

    def test_rata_rata(self):
        hasil = hitung_rata_rata(31, 33, 29)
        self.assertEqual(hasil, 31)

    def test_rata_rata_dua_nilai(self):
        hasil = hitung_rata_rata(30, 40)
        self.assertEqual(hasil, 35)

    def test_suhu_tertinggi_dan_terendah(self):
        data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Minggu", "suhu": 28}
        ]

        hasil = analisis_suhu(data)

        self.assertEqual(hasil[1]["suhu"], 35)
        self.assertEqual(hasil[2]["suhu"], 28)

    def test_jumlah_hari_panas(self):
        data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Jumat", "suhu": 32}
        ]

        hasil = analisis_suhu(data)

        self.assertEqual(hasil[3], 2)

    def test_kategori_suhu(self):
        data = [
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Minggu", "suhu": 28}
        ]

        analisis_suhu(data)

        self.assertEqual(data[0]["kategori"], "Panas")
        self.assertEqual(data[1]["kategori"], "Normal")

if __name__ == "__main__":
    unittest.main()

