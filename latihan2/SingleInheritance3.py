class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan bermotor ini sedang berjalan.")

class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
            print("Sepeda motor yamaha biru ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "Yamaha", "Biru", 150)
motorA.berkendara() # Output: Kendaraan bermotor ini sedang berjalan.
motorA.belok() # Output: Sepeda motor yamaha biru ini sedang belok.
