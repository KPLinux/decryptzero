import cv2
import numpy as np
import imutils
import argparse
from boxdetect import config
from boxdetect.pipelines import get_boxes

def align_images(image, template, maxFeatures = 500, keepPercent = 0.2, debug = False):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB.create(maxFeatures)
    (kpsA, descsA) = orb.detectAndCompute(imageGray, None)
    (kpsB, descsB) = orb.detectAndCompute(templateGray, None)
    method = cv2.DescriptorMatcher_BRUTEFORCE_HAMMING
    matcher = cv2.DescriptorMatcher_create(method)
    matches = matcher.match(descsA, descsB, None)
    matches = sorted(matches, key = lambda x:x.distance)
    keep = int(len(matches) * keepPercent)
    matches = matches[:keep]
    if debug:
        matchedVis = cv2.drawMatches(image, kpsA, template, kpsB, matches, None)
        matchedVis = imutils.resize(matchedVis, width = 1000)
        cv2.imshow("Matched Keypoints", matchedVis)
        cv2.waitKey(0)
    ptsA = np.zeros((len(matches), 2), dtype = "float")
    ptsB = np.zeros((len(matches), 2), dtype = "float")
    for (i, m) in enumerate(matches):
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt
    (H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)
    (h, w) = template.shape[:2]
    aligned = cv2.warpPerspective(image, H, (w, h))
    return aligned

def bold_images(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)

    kernel = np.ones((3, 3), np.uint8)
    bold_image = cv2.erode(thresh, kernel, iterations=1)
    bold_image = cv2.bitwise_not(bold_image)
    return bold_image

def boxing_alg(template, cfg_list):

    bold_image = bold_images(template)

    cfg = config.PipelinesConfig()

    cfg.width_range = cfg_list[0]
    cfg.height_range = cfg_list[1]
    cfg.wh_ratio_range = cfg_list[2]
    cfg.scaling_factors = cfg_list[3]
    cfg.group_size_range = (1, 1)
    cfg.dilation_iterations = 0

    rects, grouping_rects, image, output_image = get_boxes(bold_image, cfg=cfg, plot=False)

    print(grouping_rects)

    return [rects, grouping_rects, image, output_image]

def arg_maker(args_in, required, help):
    ap = argparse.ArgumentParser()
    for arg in range(len(args_in)):
        ap.add_argument("--" + args_in[arg], required = required[arg], help = help[arg])
    args_out = vars(ap.parse_args())

    return args_out

def create_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
