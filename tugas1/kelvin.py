class keltemp:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def celcius(self):
        return (self.kelvin - 273) 
    def fahrenheit(self):
        return 9/5 * (self.kelvin - 273) + 32
    def reamur(self):
        return 4/5 * (self.kelvin - 273)
    
    print("Suhu Kelvin")
kel1 = keltemp(11)
print(f"Konversi dari Kelvin ke Celcius: {kel1.celcius()}")
kel2 = keltemp(22)
print(f"Konversi dari Kelvin ke Fahrenheit: {kel2.fahrenheit()}")
kel3 = keltemp(33)
print(f"Konversi dari Kelvin ke Reamur: {kel3.reamur()}")