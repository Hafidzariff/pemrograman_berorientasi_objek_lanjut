class reatemp:
    def __init__(self, reamur):
        self.reamur = reamur

    def celcius(self):
        return (5/4 * self.reamur)
    def fahrenheit(self):
        return (9/4 * self.reamur) + 32
    def kelvin(self):
        return (5/4 * self.reamur) + 273
    
    print("Suhu Reamur")
rea1 = reatemp(88)
print(f"Konversi dari Reamur ke Celcius: {rea1.celcius()}")
rea2 = reatemp(99)
print(f"Konversi dari Reamur ke Fahrenheit: {rea2.fahrenheit()}")
rea3 = reatemp(0)
print(f"Konversi dari Reamur ke Kelvin: {rea3.kelvin()}")
print("="*44)