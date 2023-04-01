class Hewan:
    def __init__(self, nama, species, suara):
        self.nama = nama
        self.species = species
        self.suara = suara

    def bersuara(self):
        print(self.suara)


class Mammalia(Hewan):
    def __init__(self, nama, species, suara, kaki):
        super().__init__(nama, species, suara)
        self.kaki = kaki

    def berjalan(self):
        print(f"{self.nama} berjalan dengan {self.kaki} kaki.")


class paus(Mammalia):
    def __init__(self, nama, ras, ekor):
        super().__init__(nama, "paus", "orka", ekor)
        self.ras = ras

    def mengaung(self):
        print(f"{self.nama} bersuara oummmmmm.")


class sapi(Mammalia):
    def __init__(self, nama, ras, kaki):
        super().__init__(nama, "sapi", "brahman", kaki)
        self.ras = ras

    def menyeruduk(self):
        print(f"{self.nama} menyeruduk orang.")


pausA = paus("biru", "hiu paus", 4)
sapiA = sapi("mouu", "simental", 4)

pausA.bersuara()
pausA.mengaung()
pausA.berjalan()
print("------------------------")

sapiA.bersuara()
sapiA.berjalan()()
sapiA.menyeruduk()