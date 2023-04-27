my_dict = {"nama": "bambang", "umur": 20}

try:
    print(my_dict["alamat"])
except KeyError:
    print("Key tidak ditemukan! Mohon pastikan key sudah benar dan ada di dalam dictionary.")