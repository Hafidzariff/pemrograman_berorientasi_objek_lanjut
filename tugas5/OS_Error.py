try:
    file = open("filengaco.txt", "r")
except OSError as error:
    print(error)