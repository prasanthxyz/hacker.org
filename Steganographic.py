with open('boxes.gif', 'r', encoding='utf8', errors='ignore') as img:
    data = img.read()
    print(data[-14:-1])
