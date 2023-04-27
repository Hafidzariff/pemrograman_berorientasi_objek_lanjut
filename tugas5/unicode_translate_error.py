try:
    s = '你好世界'
    s.encode('ascii')
except UnicodeTranslateError:
    print("Error: Failed to translate the string to ASCII encoding")