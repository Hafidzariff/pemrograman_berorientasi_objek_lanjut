class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
    def get_nama(self):
        return self.nama
    
class Mobil(Kendaraan):
    def __init__(self, nama, merek):
        super().__init__(nama)
        self.merek = merek
    def get_merek(self):
        return self.merek
    
class SepedaMotor(Kendaraan):
    def __init__(self, nama, tipe):
        super().__init__(nama)
        self.tipe = tipe
    def get_tipe(self):
        return self.tipe
    
# turunan Hierarchical Inheritance
class Truk(Mobil):
    def __init__(self, nama, merek, kapasitas):
        super().__init__(nama, merek)
        self.kapasitas = kapasitas
    def get_kapasitas(self):
        return self.kapasitas
    
# turunan Hierarchical Inheritance
class MotorListrik(SepedaMotor):
    def __init__(self, nama, tipe, daya):
        super().__init__(nama, tipe)
        self.daya = daya
    def get_daya(self):
        return self.daya