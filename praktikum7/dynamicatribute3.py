class hewan:
    def __init__(self, nama,jenis):
        self.nama = nama
        self.jenis =jenis

h = hewan("harimau", "predator")

h.khas = "sumatra"

h.jenis = "mamalia"
print(h.nama)
print(h.jenis)
print(h.khas)