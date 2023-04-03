from abc import ABC, abstractmethod

class kendaraan(ABC):
    @abstractmethod
    def start(self):
        pass

class pesawat(kendaraan):
    def start(self):
        print("pesawat dinyalakan dengan airplane mode")

class kereta(kendaraan):
    def start(self):
        print("motor dinyalakan dengan cara menyalahkan mesin")

class traktor(kendaraan):
    def start(self):
        print("traktor dinyalakan dengan cara di starter")



P = pesawat()
K = kereta()
T = traktor()

P.start()    
K.start()    
T.start()    