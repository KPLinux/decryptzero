from algs import boxing_alg, arg_maker, align_images
from PIL import ImageGrab
import cv2
import imutils

args = ['image', 'template']
required = [True, True]
help = ["path to image being captured", "path to template image"]

args_final = arg_maker(args, required, help)

image = cv2.imread(args_final["image"])
template = cv2.imread(args_final["template"])

cfg_list = [(340,400), (50,90), (4.5, 5.5), [1.0]]
boxes = boxing_alg(template, cfg_list)

aligned = align_images(image, template)	

formatted_boxes = []

i = 1
for box in boxes[1]:
	[a, b, c, d] = box
	cropped_image = aligned[b:b+d, a:a+c]
# cv2.imshow("Input", imutils.resize(image, width = 700))
# cv2.imshow("Output", cropped_image)
# cv2.waitKey(0)
	cv2.imwrite("/home/kanishk/projects/ocr/samples/move-samples/move" + str(i) + ".jpg", cropped_image)
	i = i + 1