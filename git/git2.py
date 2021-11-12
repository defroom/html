from PIL import Image
flag = ''
for i in range(104):
    filename = str(i) + '.jpg'
    im = Image.open(filename)
    if im.getcolors()[0][1][0] == 255:
        flag = flag + '0'
    else:
        flag = flag + '1'
print(flag)
for i in range(0, len(flag), 8):
    print(chr(int(flag[i:i+8], 2)), end='')

