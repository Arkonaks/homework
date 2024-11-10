import os, sys
import requests
from PIL import Image

#   Открытие изображения и просмотр его харакетристик
im = Image.open('view-3d-animated-cartoon-bird_23-2150946465.ppm')
print(im.format, im.size, im.mode)
# im.show()


#   Создание маниатюры изображения заданного размера
size = (150, 50)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)

print(im.format, im.size, im.mode)

#   Конвертирование изображения в JPEG
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
