try:
    with open('file.txt', 'w', encoding='ascii') as f:
        f.write('Halo, dunia!')  
except UnicodeEncodeError:
    print("Error: Failed to encode the string with ASCII encoding")