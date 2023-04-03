class kendaraan:
    def move(self):
        print("kendaraan berjalan")

class pesawat(kendaraan):
    def move(self):
        print("pesawat berjalan terbang")

class kereta(kendaraan):
    def move(self):
        print("kerta berjalan")

K = kendaraan()
P = pesawat()
Ke = kereta()

K.move()    
P.move()    
Ke.move()    