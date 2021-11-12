with open('0.jpg', 'rb') as f1, open('1.jpg', 'rb') as f2:
    white = f1.read()
    black = f2.read()
flag = ""
for i in range(0, 104):
    filename = str(i) + ".jpg"
    with open(filename, 'rb') as f:
        txt = f.read()
        if txt == white:
            flag = flag + '0'
        elif txt == black:
            flag = flag + '1'
print(flag)
for i in range(0, len(flag), 8):
    print(chr(int(flag[i:i+8], 2)), end='')