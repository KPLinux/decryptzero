from algs import align_images, arg_maker, boxing_alg, bold_images
from collections import namedtuple
import easyocr
import cv2
import imutils

reader = easyocr.Reader(['en'], gpu = True, recog_network='decryptzero2')

result = reader.readtext('./sample/image.png')
print(result)