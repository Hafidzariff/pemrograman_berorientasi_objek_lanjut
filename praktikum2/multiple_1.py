class motor:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc
    
    def servis(self):
        print(self.nama, "sedang di servis")

class matic:
    def __init__(self, nama, transmisi):
        self.nama = nama
        self.transmisi = transmisi

    def modif(self):
        print(self.nama, "sedang di modif")

class MotorMatic(motor, matic):
    def __init__(self, nama, cc, transmisi):
        motor.__init__(self, nama, cc)
        matic.__init__(self, nama, transmisi)

    def uji(self):
        print(self.nama, "sedang di uji kelayakan")
        
motor_at = MotorMatic("mio", "150", "Automatic")
motor_at.servis() 
motor_at.modif() 
motor_at.uji() 