from algs import align_images, arg_maker, boxing_alg, bold_images
from collections import namedtuple
import easyocr
import cv2
import imutils

reader = easyocr.Reader(['en'], gpu = True, recog_network='decryptzero')

def clean_text(text):
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

args = ['image', 'align-template', 'box-template']
required = [True, True, True]
help = ["path to image being aligned with template", "path to alignment template image", "path to boxing template image"]

args_final = arg_maker(args, required, help)

print("[INFO] loading images...")
image = cv2.imread(args_final["image"])
align_template = cv2.imread(args_final["align_template"])
box_template = cv2.imread(args_final["box_template"])

print("[INFO] aligning images...")
aligned = align_images(image, align_template)
cv2.imshow('aligned', imutils.resize(aligned, width=700))

print("[INFO] OCR'ing document...")
parsingResults = []

OCRLocation = namedtuple("OCRLocation", ["id", "bbox", "filter_keywords"])
OCR_LOCATIONS = []

cfg_list = [(340,400), (50,90), (4.5, 5.5), [1.0]]
boxes = boxing_alg(box_template, cfg_list)

for i in range(len(boxes[1])):
	if i % 2 == 1:
		OCR_LOCATIONS.append(OCRLocation("move" + str(i) + "_white", boxes[1][i], []))
	elif i % 2 == 0:
		OCR_LOCATIONS.append(OCRLocation("move" + str(i) + "_black", boxes[1][i], []))
j = 0
for loc in OCR_LOCATIONS:
	(x, y, w, h) = loc.bbox
	roi = aligned[y:y + h, x:x + w]
	bold = bold_images(roi)
	cv2.imshow('output', bold)
	text = reader.readtext(bold)
	print(text)
	j += 1
	if j == 1:
	    break
cv2.waitKey(0)