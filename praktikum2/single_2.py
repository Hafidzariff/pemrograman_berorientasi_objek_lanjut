class Motor:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc

    def kecepatan(self):
        print(f"{self.nama} berkecepatan tinggi")

class kawasaki(Motor):
    def __init__(self, nama, cc, jenis):
        super().__init__(nama, cc)
        self.jenis = jenis

    def balapan(self):
        print(f"{self.nama} dengan jenis {self.jenis} sedang balapan")
        
kawasakiA = kawasaki("Ninja", 250, "R")
kawasakiA.kecepatan() 
kawasakiA.balapan() 