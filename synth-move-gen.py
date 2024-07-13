from trdg.generators import GeneratorFromStrings
from tqdm.auto import tqdm
import os
import pandas as pd
import numpy as np
import random
from algs import create_file

NUM_IMAGES_TO_SAVE = 10

pieces_list = ['B', 'N', 'R', 'Q', 'K']
files_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks_list = ['1', '2', '3', '4', '5', '6', '7', '8']
spec_char_list = ['', '', '', '', '', '', '', '+', '+', '#']
gen_moves_list = []

def rand_move_gen(moves_list):
    rand_piece = random.choice(pieces_list)
    if rand_piece != 'K':    
        moves_list.append(rand_piece + random.choice(files_list) + random.choice(ranks_list) + random.choice(spec_char_list))
    else:
        moves_list.append(rand_piece + random.choice(files_list) + random.choice(ranks_list))
    return moves_list

for i in range(100):
    rand_move_gen(gen_moves_list)

print(gen_moves_list)

generator = GeneratorFromStrings(
    gen_moves_list,
    is_handwritten=True
)

print(generator)

i = 92

# for img, lbl in generator:
#     img.save("/home/kanishk/projects/ocr/samples/move-samples/" + str(i) + ".png")
#     create_file(str(i) + ".gt.txt", lbl)

f = open("/home/kanishk/projects/ocr/labels.txt", "a")

for counter, (img, lbl) in tqdm(enumerate(generator), total = NUM_IMAGES_TO_SAVE):
    if (counter >= NUM_IMAGES_TO_SAVE):
        break
    # img.show()
    #save pillow image
    img.save(f'/home/kanishk/projects/ocr/samples/move-samples/{i}.png')
    f.write(f'{i}.png {lbl}\n')
    i += 1
    # Do something with the pillow images here.
f.close()