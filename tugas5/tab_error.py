try:

    for i in range(5):
        print(i)
        if i == 2:
            print("Item ke-2")
            print("Sedang dijalankan") 
except TabError as e:
    print("Terjadi TabError:", e)
