import easyocr
import cv2
reader = easyocr.Reader(['en'], recog_network='decryptzero')

img_path = '/home/kplinux/projects/ocr/samples/move-samples/move10.jpg'
img = cv2.imread(img_path)

result = reader.readtext(img)
print(result)