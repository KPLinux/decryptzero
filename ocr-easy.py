from algs import align_images, arg_maker, boxing_alg, bold_images
from collections import namedtuple
import easyocr
import cv2
import imutils
import matplotlib.pyplot as plt

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
	
for loc in OCR_LOCATIONS:
	(x, y, w, h) = loc.bbox
	roi = aligned[y:y + h, x:x + w]
	rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
	bold = bold_images(rgb)
	text = reader.readtext(bold)
	if len(text) == 0:
		continue
	else: 
		print(text[0][1])
	for line in text[0][1]:
		if len(line) == 0:
			continue
		parsingResults.append((loc, line))

results = {}
for (loc, line) in parsingResults:
	r = results.get(loc.id, None)
	if r is None:
		results[loc.id] = (line, loc._asdict())
	else:
		(existingText, loc) = r
		text = "{}\n{}".format(existingText, line)
		results[loc["id"]] = (text, loc)

for (locID, result) in results.items():
	(text, loc) = result
	print(loc["id"])
	print("=" * len(loc["id"]))
	print("{}\n\n".format(text))
	(x, y, w, h) = loc["bbox"]
	clean = clean_text(text)
	cv2.rectangle(aligned, (x, y), (x + w, y + h), (0, 255, 0), 2)
	for (i, line) in enumerate(text.split("\n")):
		startY = y + (i * 70) + 40
		cv2.putText(aligned, line, (x, startY),
			cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 255), 5)

cv2.imshow("Input", imutils.resize(image, width=700))
cv2.imshow("Output", imutils.resize(aligned, width=700))
cv2.waitKey(0)