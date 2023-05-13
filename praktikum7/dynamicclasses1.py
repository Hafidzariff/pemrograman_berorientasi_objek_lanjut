def custom_kendaraan(tipe_kendaraan):
    class kendaraan:
        def __init__(self, brand, warna):
            self.tipe_kendaraan = tipe_kendaraan
            self.brand = brand
            self.warna = warna

        def __repr__(self):
            return f"{self.brand} {self.tipe_kendaraan} ({self.warna})"

    return kendaraan


Bike = custom_kendaraan("Sepeda")
Motorcycle = custom_kendaraan("Motor")


bike1 = Bike("Exotic", "Biru")
bike2 = Bike("Pasific", "Hijau")

motorcycle1 = Motorcycle("Yamaha", "Biru")
motorcycle2 = Motorcycle("Honda", "Kuning")

print(bike1)  
print(bike2)  

print(motorcycle1)  
print(motorcycle2)  
