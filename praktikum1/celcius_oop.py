#Hafidz arif
#221511021
#Praktikum-1 PBO2 2023 
#TI22K

class tempconv:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_reamur(self):
        return (4/5) * self.celcius
    
    def to_kelvin(self):
        return self.celcius + 273.15
    
    def to_fahrenheit(self):
        return (9/5) * self.celcius + 32
    
temp = tempconv(12)
fahrenheit = temp.to_fahrenheit()
kelvin = temp.to_kelvin()
reamur = temp.to_reamur()
print(f"{temp.celcius} derajat Celcius = {reamur} Reamur")
print(f"{temp.celcius} derajat Celcius = {kelvin} Kelvin")
print(f"{temp.celcius} derajat Celcius = {fahrenheit} Fahrenheit")