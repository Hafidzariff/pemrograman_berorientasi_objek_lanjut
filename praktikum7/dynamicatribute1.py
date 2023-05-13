class pesawat:
    def __init__(self, jenis,merk):
        self.jenis = jenis
        self.merk =merk

m = pesawat("Airbus", "A320")

m.varian = "A320neo"

m.merk = "Nissan"
print(m.jenis)
print(m.merk)
print(m.varian)