try:
    big_list = [1] * (10**9)
except MemoryError:
    print("Terjadi error MemoryError. List terlalu besar untuk di-handle!")