class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_jurnal(self, judul, isi):
        jurnal = Jurnal(judul, isi, self)
        return jurnal
    
class Jurnal:
    def __init__(self, judul, isi, penulis):
        self.judul = judul
        self.isi = isi
        self.penulis = penulis

p1 = Peneliti("dody heriyanto", "game")


j1 = p1.tulis_jurnal("bagaimana cara bermain permainan sodoku ", "pelatihan ini untuk mengajarkan bermain sodoku yang benar")


print(j1.judul)
print(j1.penulis.nama)