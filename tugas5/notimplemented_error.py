class Animal:
    def sound(self):
        raise NotImplementedError("Method 'sound' belum diimplementasikan")

class Cat(Animal):
    def sound(self):
        return "Meow"

class Dog(Animal):
    pass

def make_sound(animal):
    try:
        return animal.sound()
    except NotImplementedError as error:
        print(error)

cat = Cat()
dog = Dog()

print(make_sound(cat))
print(make_sound(dog))