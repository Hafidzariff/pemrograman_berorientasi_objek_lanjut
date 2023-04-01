class kendaraan:
    def __init__(self, nyala, model, tahun, berat):
        self.nyala = nyala
        self.model = model
        self.tahun = tahun
        self.berat = berat

    def nyalakan_mesin(self):
        print(f"Mesin {self.nyala} {self.model} di nyalakan.")

    def matikan_mesin(self):
        print(f"Mesin {self.nyala} {self.model} di matikan")

class mobil(kendaraan):
    def __init__(self, nyala, model, tahun, berat, jml_pintu):
        super().__init__(nyala, model, tahun, berat)
        self.jml_pintu = jml_pintu

    def memiliki_pintu(self):
        print(f"Mobil {self.nyala} {self.model} Memiliki {self.jml_pintu} pintu")

class motor(kendaraan):
    def __init__(self, nyala, model, tahun, berat, jml_roda):
        super().__init__(nyala, model, tahun, berat)
        self.jml_roda = jml_roda

    def berjalan(self):
        print(f"Motor {self.nyala} {self.model} berjalan dengan {self.jml_roda} roda.")

class mbl_listrik(mobil):
    def __init__(self, nyala, model, tahun, berat, jml_pintu, kapasitas_baterai):
        super().__init__(nyala, model, tahun, berat, jml_pintu)
        self.kapasitas_baterai = kapasitas_baterai

    def charge_baterai(self):
        print(f"Mobil {self.nyala} {self.model} memiliki kapasitas baterai {self.kapasitas_baterai} kWh.")

class Electricmotor(motor):
    def __init__(self, nyala, model, tahun, berat, jml_roda, kapasitas_baterai):
        super().__init__(nyala, model, tahun, berat, jml_roda)
        self.kapasitas_baterai = kapasitas_baterai

    def charge_baterai(self):
        print(f"Motor {self.nyala} {self.model} memiliki kapasitas baterai {self.kapasitas_baterai} kWh.")

mobilA = mobil("Toyota", "Inova", 2022, 1200, 4)
mobilA.nyalakan_mesin()
mobilA.memiliki_pintu()
mobilA.matikan_mesin()

motorA = motor("Honda", "Supra X", 2021, 250, 2)
motorA.nyalakan_mesin()
motorA.berjalan()
motorA.matikan_mesin()

ev = mbl_listrik("Wuling", "Air Ev", 2023, 2000, 4, 100)
ev.nyalakan_mesin()
ev.charge_baterai()
ev.charge_baterai()
ev.matikan_mesin()

e_bike = Electricmotor("flywin", "01", 2023, 300, 2, 15.5)
e_bike.nyalakan_mesin()
e_bike.charge_baterai()
e_bike.charge_baterai()
e_bike.matikan_mesin()