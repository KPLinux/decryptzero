from algs import create_file
import os
import re

def extract_index(filename):
    match = re.search(r'\d+', filename)  # Extract number from filename
    return int(match.group()) if match else float('inf')  # Return number or infinity if not found

i = 0
for file in sorted(os.listdir('/home/kplinux/projects/ocr/decrypt-trainer/eval-no-transform2/samples'),
                   key = extract_index):
    with open('/home/kplinux/projects/ocr/decrypt-trainer/eval-no-transform2/gt.txt', 'a') as f:
        f.write('samples/' + file + '\t' + file.replace(str(i) + '__', '').replace('.png', '') + '\n')
    i += 1