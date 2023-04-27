try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
except UnicodeDecodeError:
    print("Error: Failed to decode the file with UTF-8 encoding")