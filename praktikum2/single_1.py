class Kuliner:
    def __init__(self, nama, daerah):
        self.nama = nama
        self.daerah = daerah

    def khas(self):
        print(self.nama, "makanan khas indonesia")
        
class Jogja(Kuliner):
    def __init__(self, nama, karakter, jenis_makanan):
        super().__init__(nama, karakter)
        self.jenis_makanan = jenis_makanan
        
    def rasa(self):
        print("cenderung manis")
        
jogjaA = Jogja("Gudeg","Nasi" , "Berat")
jogjaA.khas() 
jogjaA.rasa() 