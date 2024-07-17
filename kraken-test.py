import kraken
from kraken import pageseg, rpred
with open('/home/kplinux/projects/ocr/samples/sheet-samples/uscf-commem-pencil.jpg', 'rb') as img:
    image = pageseg.segment(img.read())

model = rpred.load_any('/home/kplinux/.config/kraken/en_best.mlmodel')
text = rpred.recognize(image, model)
print(text)