import os
import glob
import cv2
import matplotlib.pyplot as plt

def main():
    directory="inp_chars"
    names_list=["a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", "R", "N", "K", "Q", "B", "=", "+", "x", "#"]
    label_images(directory, names_list)


def get_next_suffix(directory, name):
    suffix=1
    while os.path.exists(os.path.join(directory, f"{name}_{suffix}.png")):
        suffix += 1
    return suffix

def display_image(image_path):
    image=cv2.imread(image_path)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def label_images(directory, names_list):
    files=glob.glob(os.path.join(directory, "*.png"))
    unlabeled_files=[file for file in files if not any(file.startswith(os.path.join(directory, name)) for name in names_list)]
    for file_path in unlabeled_files:
        display_image(file_path)
        name=input(f"Enter a name from {names_list}: ").strip()
        if name in names_list:
            suffix=get_next_suffix(directory, name)
            new_file_name=f"{name}_{suffix}.png"
            new_file_path=os.path.join(directory, new_file_name)

            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")
        else:
            print(f"Invalid name. Please enter a name from {names_list}.")

if __name__=="__main__":
    main()
