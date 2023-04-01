class hewan:
    def __init__(self, nama, species, umur):
        self.nama = nama
        self.species = species
        self.umur = umur

    def gerak(self):
        print(f" {self.species} bernama {self.nama} sedang bergerak.")

    def makan(self):
        print(f" {self.species} bernama {self.nama} sedang makan.")

class mamalia(hewan):
    def __init__(self, nama, species, umur, jml_kaki):
        super().__init__(nama, species, umur)
        self.jml_kaki = jml_kaki

    def melahirkan(self):
        print(f"  {self.species} bernama {self.nama} telah melahirkan.")

class burung(hewan):
    def __init__(self, nama, species, umur, warna_bulu):
        super().__init__(nama, species, umur)
        self.warna_bulu = warna_bulu

    def warna(self):
        print(f" {self.species} bernama {self.nama} memiliki warna bulu {self.warna_bulu} ")

class reptil(hewan):
    def __init__(self, nama, species, umur, habitat):
        super().__init__(nama, species, umur)
        self.habitat = habitat

    def hidup(self):
        print(f" {self.species} bernama {self.nama} banyak hidup di {self.habitat} ")

class anjing(mamalia):
    def __init__(self, nama, umur, ras, jml_kaki):
        super().__init__(nama, "anjing", umur, jml_kaki)
        self.ras = ras

    def menggonggong(self):
        print(f" {self.nama} bernama {self.ras} suka menggonggong")

class beo(burung):
    def __init__(self, nama, umur, warna_bulu, bicara):
        super().__init__(nama, "beo", umur, warna_bulu)
        self.bicara = bicara

    def ngomong(self):
        if self.bicara:
            print(f"beo bernama {self.nama} suka ngomong")
        else:
            print(f"beo bernama {self.nama} ga bisa ngomong")

class ular(reptil):
    def __init__(self, nama, umur, habitat, berbisa):
        super().__init__(nama, "ular", umur, habitat)
        self.berbisa = berbisa

    def menggigit(self):
        if self.berbisa:
            print(f"ular bernama {self.nama} memiliki bisa")
        else:
            print(f"ular bernama {self.nama} tidak berbisa")

anjing = anjing("guguk", 3, "kintamani", 4)
anjing.gerak()
anjing.makan()
anjing.melahirkan()
anjing.menggonggong()

beo = beo("ngomul", 3, "merah", True)
beo.gerak()
beo.makan()
beo.warna()
beo.ngomong()

ular = ular("mamba", 3, "semak semak", True)
ular.gerak()
ular.makan()
ular.hidup()
ular.menggigit()