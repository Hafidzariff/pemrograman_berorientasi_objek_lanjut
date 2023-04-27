def print_unicode_char(text):
    try:
        print(text.encode('ascii').decode('utf-8'))
    except UnicodeError as e:
        print("Error:", e)
        print("Could not process Unicode character.")

print_unicode_char('Hello, world!') 
print_unicode_char('Héllo, wórld!') 