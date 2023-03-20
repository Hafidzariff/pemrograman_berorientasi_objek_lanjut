class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y    

print(Kalkulator.add(3,5))
print(Kalkulator.subtract(10, 7))
print(Kalkulator.multiply(4,6))
print(Kalkulator.divide(12,4))
