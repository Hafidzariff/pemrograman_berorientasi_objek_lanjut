class menu:
    def __init__(self, nama,harga):
        self.nama = nama
        self.harga =harga

m = menu("gacoan", "10000")

m.variasi = "dimsum"

m.harga = "10000"
print(m.nama)
print(m.harga)
print(m.variasi)