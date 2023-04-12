class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
    
class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []
    
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

m1 = Mahasiswa("dody heriyanto", "201222")
k9 = KelompokKKM("Kelompok 9")
m1.gabung_kelompok(k9)


print(k9.nama)
for anggota in k9.anggota:
    print(anggota.nama)