class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis

    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")

class Mamalia(Hewan):
    def __init__(self, jenis, nama):
        super().__init__(jenis)
        self.nama = nama

    def display_info(self):
        super().display_info()
        print(f"Nama mamalia: {self.nama}")

class Karnivora(Hewan):
    def __init__(self, jenis, Makanan):
        super().__init__(jenis)
        self.Makanan = Makanan

    def display_info(self):
        super().display_info()
        print(f"Jenis Makanan: {self.Makanan}")

class Harimau(Mamalia, Karnivora):
    def __init__(self, jenis, nama, Makanan):
        Mamalia.__init__(self, jenis, nama)
        Karnivora.__init__(self, jenis, Makanan)

    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")
        
# contoh penggunaan
harimauA = Harimau("Mamalia", "Paus Biru", "Plankton")
harimauA.display_info()
