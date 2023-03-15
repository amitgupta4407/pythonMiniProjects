from PIL import Image
import os

os.chdir(r'D:\test')
img = Image.open('1.png')
img.convert("P", palette=Image.ADAPTIVE, colors=8)
img.save(r'D:\test\2.png')