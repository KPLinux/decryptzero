import cv2
import imutils
import numpy as np
from algs import align_images, arg_maker

args = ['image', 'template']
required = [True, True]
help = ["path to image being aligned with template", "path to template image"]

args_final = arg_maker(args, required, help)

print("[INFO] loading images...")
image = cv2.imread(args_final["image"])
template = cv2.imread(args_final["template"])

print("[INFO] aligning images...")
aligned = align_images(image, template, debug = True)

aligned = imutils.resize(aligned, width = 700)
template = imutils.resize(template, width = 700)
stacked = np.hstack([aligned, template])

overlay = template.copy()
output = aligned.copy()
cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

cv2.imshow("Image Alignment Stacked", stacked)
cv2.imshow("Image Alignment Overlay", output)
cv2.waitKey(0)