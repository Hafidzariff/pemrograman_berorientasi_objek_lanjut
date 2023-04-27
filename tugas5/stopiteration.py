my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

try:
    while True:
        item = next(my_iterator)
        print(item)
        if item == 3:
            raise StopIteration
except StopIteration:
    print("Iteration stopped!")