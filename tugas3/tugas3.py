#pastikan modul playsound sudah terinstall
from playsound import playsound

class Hewan:
    suara = "gaada.mp3"

    def mainkan_suara(self):
        playsound(self.suara)

class Angsa(Hewan):
    suara = "angsa.mp3"

class Babi(Hewan):
    suara = "babi.mp3"

class Burunghantu(Hewan):
    suara = "burunghantu.mp3"

class Burungmakau(Hewan):
    suara = "burungmakau.mp3"

class Burungmerak(Hewan):
    suara = "burungmerak.mp3"

class Burungmockingbird(Hewan):
    suara = "burungmockingbird.mp3"

class Gajah(Hewan):
    suara = "gajah.mp3"

class Kera(Hewan):
    suara = "kera.mp3"

class Macan(Hewan):
    suara = "macan.mp3"

class Singa(Hewan):
    suara = "singa.mp3"

#instansiasi
angsa=Angsa()
babi=Babi()
burunghantu=Burunghantu() 
burungmakau=Burungmakau()
burungmerak=Burungmerak()
burungmockingbird=Burungmockingbird()
gajah=Gajah()
kera=Kera()
macan=Macan()
singa=Singa()

#contoh pemanggilan
angsa.mainkan_suara()
babi.mainkan_suara()
burunghantu.mainkan_suara()
burungmakau.mainkan_suara()
burungmerak.mainkan_suara()
burungmockingbird.mainkan_suara()
gajah.mainkan_suara()
kera.mainkan_suara()
macan.mainkan_suara()
singa.mainkan_suara()

#apa bila terjadi error coba upgrade/downgrade ke module playsound versi 1.2.2

