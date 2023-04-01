class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

dosenA = Dosen("Hafidz arif", 19, "221511021")
dosenA.berbicara() # Output: Hafidz arif sedang berbicara.
dosenA.mengajar() # Output: Hafidz arif dengan NIP 221511021 sedang mengajar.