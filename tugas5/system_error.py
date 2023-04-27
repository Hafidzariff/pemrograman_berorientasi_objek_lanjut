def my_function(n):
    if n <= 0:
        raise SystemError("Jumlah iterasi harus lebih dari 0")
    for i in range(n):
        print(i)
        
try:
    my_function(-1)
except SystemError as e:
    print("Terjadi SystemError:", e)