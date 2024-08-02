from algs import boxing_alg, arg_maker
from boxdetect import config
from boxdetect.pipelines import get_boxes
import matplotlib.pyplot as plt
import cv2
import numpy as np
import argparse
import imutils

args = ['template']
required = [True]
help = ["template"]
args_final = arg_maker(args, required, help)

file_path = cv2.imread(args_final["template"])

cfg_list = [(340,400), (50,90), (4.5, 5.5), [12.0]]

plt.figure(figsize = (20,20))
plt.imshow(boxing_alg(file_path, cfg_list)[3])
plt.show()
