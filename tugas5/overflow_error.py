import sys

try:
    x = sys.maxsize + 1
    y = x * x
except OverflowError as error:
    print(error)