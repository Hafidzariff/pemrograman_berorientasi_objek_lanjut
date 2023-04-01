class hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def berbunyi(self):
        pass
    
class mamalia(hewan):
    def __init__(self, nama):
        super().__init__(nama)
    
    def melahirkan(self):
        pass
    
class anjing(mamalia):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "guk guk"
    
class kucing(mamalia):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "meong"
    
class burung(hewan):
    def __init__(self, nama):
        super().__init__(nama)
    
    def fly(self):
        pass
    
class beo(burung):
    def __init__(self, nama):
        super().__init__(nama)
    
    def berbunyi(self):
        return "assalamualaikum"
    
anjingA = anjing("bleki")
kucingA = kucing("oyen")
beoA = beo("bribin")

print(anjingA.nama + ": " + anjingA.berbunyi())
print(kucingA.nama + ": " + kucingA.berbunyi())
print(beoA.nama + ": " + beoA.berbunyi())