import math

try:
    result = math.sqrt(-1)
    print(result)
except FloatingPointError as error:
    print(error)