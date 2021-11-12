from PIL import Image
im = Image.open('d:/git/html/file/a.gif')
im.tell()
im.save('0.png')
im.seek(1)
im.save('1.png')
im.seek(2)
im.save('2.png')