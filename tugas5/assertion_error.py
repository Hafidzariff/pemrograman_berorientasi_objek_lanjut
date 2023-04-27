def divide(num1, num2):
    assert num2 != 0, "tidak bisa di bagi 0"
    return num1 / num2

try:
    result = divide(10, 0)
    print(result)
except AssertionError as error:
    print(error)