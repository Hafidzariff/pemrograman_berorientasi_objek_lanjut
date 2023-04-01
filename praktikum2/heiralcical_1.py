class pegawai:
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji

    def display_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Gaji:", self.gaji)


class Manager(pegawai):
    def __init__(self, name, umur, gaji, department):
        super().__init__(name, umur, gaji)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)


class SalesManager(Manager):
    def __init__(self, nama, umur, gaji, department, bonus):
        super().__init__(nama, umur, gaji, department)
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print("Bonus:", self.bonus)


class HRManager(Manager):
    def __init__(self, nama, umur, gaji, department, tunjangan):
        super().__init__(nama, umur, gaji, department)
        self.tunjangan = tunjangan

    def display_info(self):
        super().display_info()
        print("Tunjangan:", self.tunjangan)


pegawaiA = pegawai("wahyu", 20, 6000)
managerA = Manager("aji harka", 21, 50000, "Kyai")
smA = SalesManager("nopal", 25, 15000, "Pengerus", 5000)
hrA = HRManager("upi", 40, 20000, "santri", 10000)

pegawaiA.display_info()
print("------------------------")
managerA.display_info()
print("------------------------")
smA.display_info()
print("------------------------")
hrA.display_info()