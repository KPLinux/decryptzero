import os
import random
import glob
import cv2
import numpy as np

pieces_list=['B', 'K', 'N', 'Q', 'R']
files_list = ['a' 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks_list=['1', '2', '3', '4', '5', '6', '7', '8']
endings=['+', '#']
promotion=['=']
captures=['x']
cast=['O', '-', 'O']

def main():
    global transformations
    directory="inp_chars"
    samples_dir="samples"

    #whether you want to have transformations or not
    transformations=False

    if not os.path.exists(samples_dir):
        os.makedirs(samples_dir)
    for i in range(10):
        cending=random.randint(0,8)
        if cending==1:
            cending=True
        else:
            cending=False
        ccapt=random.randint(0,3)
        if ccapt==1:
            ccapt=True
        else:
            ccapt=False
        ccast=random.randint(0,10)
        if ccast==1:
            ccast=True
        else:
            ccast=False
        cpromo=random.randint(0,10)
        if cpromo==1:
            cpromo=True
        else:
            cpromo=False
        gen_img(directory, samples_dir, cending, ccapt, ccast, cpromo, i)


def apply_random_transformations(image):
    wellaligned=random.randint(1,19) # lol give a little higher chance of having a better aligned image cause we tend to
    if wellaligned != 5:
        angle=random.uniform(-30, 30)
    else:
        angle=0
    height, width=image.shape[:2]
    rotation_matrix=cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image=cv2.warpAffine(image, rotation_matrix, (width, height), borderValue=(255, 255, 255))

    scale=random.uniform(0.9, 1.1)
    scaled_image=cv2.resize(rotated_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def get_rand_img(directory, prefix):
    files=glob.glob(os.path.join(directory, f"{prefix}_*.png"))
    if not files:
        raise FileNotFoundError(f"no files with {prefix} in {directory}")
    return random.choice(files)

# def get_next_suffix(directory, base_name):
    # suffix=1
    # while os.path.exists(os.path.join(directory, f"{suffix}__{base_name}.png")):
    #     suffix += 1
    # return suffix

def pad_image(image, height):
    if len(image.shape) == 2:  # Grayscale image
        image=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    padt=(height - image.shape[0]) // 2
    padb=height - image.shape[0] - padt
    return cv2.copyMakeBorder(image, padt, padb, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])

def combine_imgs(images):
    if transformations == True:
        transformed_images=[apply_random_transformations(img) for img in images]
        max_height=max(img.shape[0] for img in transformed_images)
        padded_images=[]
        for img in transformed_images:
            padding_top=random.randint(0, max_height - img.shape[0])
            padding_bottom=max_height - img.shape[0] - padding_top
            padded_img=cv2.copyMakeBorder(img, padding_top, padding_bottom, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
            padded_images.append(padded_img)
        return cv2.hconcat(padded_images)
    else:
        max_height=max(img.shape[0] for img in images)
        padded_images=[pad_image(img, max_height) for img in images]
        return cv2.hconcat(padded_images)

def gen_img(directory, samples_dir, cending, ccapt, ccast, cpromo, suffix):
    piece=random.choice(pieces_list)
    file=random.choice(files_list)
    rank=random.choice(ranks_list)
    shach=random.choice(endings)
    capture=random.choice(captures)
    promo=random.choice(promotion)

    piece_img_path=get_rand_img(directory, piece)
    file_img_path=get_rand_img(directory, file)
    rank_img_path=get_rand_img(directory, rank)
    shach_img_path=get_rand_img(directory, shach)
    capture_img_path=get_rand_img(directory, capture)
    cast_img_path=[get_rand_img(directory, cast[i]) for i in range(len(cast))]
    promo_img_path=get_rand_img(directory, promo)

    piece_img=cv2.imread(piece_img_path)
    file_img=cv2.imread(file_img_path)
    rank_img=cv2.imread(rank_img_path)
    shach_img=cv2.imread(shach_img_path)
    capture_img=cv2.imread(capture_img_path)
    promo_img=cv2.imread(promo_img_path)

    if ccast:
        combined_img=combine_imgs([cv2.imread(cast_img_path[i]) for i in range(len(cast))])
        base_name=f"{cast[0]}{cast[1]}{cast[2]}"
    elif cpromo:
        combined_img=combine_imgs([file_img, rank_img, promo_img, piece_img])
        base_name=f"{file}{rank}{promo}{piece}"
    elif not cending and not ccapt:
        combined_img=combine_imgs([piece_img, file_img, rank_img])
        base_name=f"{piece}{file}{rank}"
    elif cending and not ccapt:
        combined_img=combine_imgs([piece_img, file_img, rank_img, shach_img])
        base_name=f"{piece}{file}{rank}{shach}"
    elif not cending and ccapt:
        combined_img=combine_imgs([piece_img, capture_img, file_img, rank_img])
        base_name=f"{piece}{capture}{file}{rank}"
    else:
        combined_img=combine_imgs([piece_img, capture_img, file_img, rank_img, shach_img])
        base_name=f"{piece}{capture}{file}{rank}{shach}"

    # suffix=get_next_suffix(samples_dir, base_name)
    output_path=os.path.join(samples_dir, f"{suffix}__{base_name}.png")

    cv2.imwrite(output_path, combined_img)
    print(f"gen image saved as {output_path}")

if __name__ == "__main__":
    main()
