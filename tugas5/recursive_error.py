def count_down(num):
    print(num)
    count_down(num - 1)

try:
    count_down(10)
except RecursionError as error:
    print(error)