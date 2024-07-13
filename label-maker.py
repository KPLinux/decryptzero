from algs import create_file

i = 1
for line in open("/home/kanishk/projects/ocr/samples/move-samples/labels.txt", 'r'):
    create_file("/home/kanishk/projects/ocr/samples/label-samples/" + str(i) + ".gt.txt", line)
    i = i + 1