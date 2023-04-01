class BangunDatar:
    def __init__(self, sisi):
        self.sisi = sisi
    def luasArea(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__(sisi)
    def luasArea(self):
        return self.sisi * self.sisi
    def Nilaikeliling(self):
        return 4 * self.sisi
    
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        super().__init__(jari_jari)
    def luasArea(self):
        return 3.14 * self.sisi * self.sisi
    def Nilaikeliling(self):
        return 2 * 3.14 * self.sisi
    
persegi = Persegi(30)
lingkaran = Lingkaran(35)
print("Luas persegi:", persegi.luasArea())
print("Keliling persegi:", persegi.Nilaikeliling())
print("Luas lingkaran:", lingkaran.luasArea())
print("Keliling lingkaran:", lingkaran.Nilaikeliling())

