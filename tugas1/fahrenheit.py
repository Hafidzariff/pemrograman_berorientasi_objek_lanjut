class fahtemp:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def celcius(self):
        return 5/9 * (self.fahrenheit - 32)
    def kelvin(self):
        return 5/9 * (self.fahrenheit - 32) +273
    def reamur(self):
        return 4/9 * (self.fahrenheit - 32)
    
    print("Suhu Fahrenheit")
fah1 = fahtemp(55)
print(f"Konversi dari Fahrenheit ke Celcius: {fah1.celcius()}")
fah2 = fahtemp(66)
print(f"Konversi dari Fahrenheit ke Kelvin: {fah2.kelvin()}")
fah3 = fahtemp(77)
print(f"Konversi dari Fahrenheit ke Reamur: {fah3.reamur()}")
print("="*44)