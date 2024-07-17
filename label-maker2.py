from algs import create_file
import os
import re

def extract_index(filename):
    match = re.search(r'\d+', filename)  # Extract number from filename
    return int(match.group()) if match else float('inf')  # Return number or infinity if not found

print(extract_index('samples988__Kc5.png'))

i = 0
for file in sorted(os.listdir('/home/kplinux/projects/ocr/deep-text-recognition-benchmark/train_data/samples'),
                   key = extract_index):
    with open('/home/kplinux/projects/ocr/deep-text-recognition-benchmark/train_data/gt.txt', 'a') as f:
        f.write('samples/' + file + '\t' + file.replace(str(i) + '__', '').replace('.png', '') + '\n')
    i += 1