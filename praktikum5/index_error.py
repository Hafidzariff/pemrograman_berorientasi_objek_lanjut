my_list = ["a", "b", "c"]

try:
    print(my_list[3])
except IndexError:
    print("Index tidak ditemukan! Mohon pastikan index sudah benar dan ada di dalam list.")