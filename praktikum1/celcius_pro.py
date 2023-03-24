#Hafidz arif
#221511021
#Praktikum-1 PBO2 2023 
#TI22K

class tempconv:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32

    @staticmethod
    def celcius_to_reamur(celcius):
        return celcius * 4/5
    
    @staticmethod
    def celcius_to_kelvin(celcius):
        return celcius + 273.15
    

# Konversi suhu 46 derajat Celsius ke Fahrenheit
fahrenheit = tempconv.celcius_to_fahrenheit(46)
print("konversi suhu",46, "derajat celcius adalah ",fahrenheit,
"derajat fahrenheit")

# Konversi suhu 13 derajat Celsius ke Reamur
reamur = tempconv.celcius_to_reamur(13)
print("konversi suhu",13, "derajat celcius adalah ",reamur,
"derajat reamur")

# Konversi suhu 22 derajat Celsius ke Kelvin
kelvin = tempconv.celcius_to_kelvin(22)
print("konversi suhu",22, "derajat celcius adalah ",kelvin,
"derajat kelvin")