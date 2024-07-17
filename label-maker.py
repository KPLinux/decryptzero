from algs import create_file

i = 0

test_string = "hello there I am Mr. Green!"

start = 0
# for i in range(len(test_string)):
    # if test_string[i] == ' ':
        # print(test_string[start:i])
        # start = i+1
# print(test_string[start:])


line_list = []
for line in open("/home/kplinux/projects/ocr/samples/labels1.txt", 'r'):
    for char in range(len(line)):
        if line[char] == ' ':
            line_list.append(line[start:char])
            start = char + 1
    line_list.append(line[start:])
    for n in line_list:
        if n == '':
            line_list.remove(n)
        line_list = list(map(lambda x: x.replace('\n',''), line_list))
    create_file("/home/kplinux/projects/ocr/samples/decrypt-ground-truth2/" 
                + str(i) + "__" + line_list[0] + ".gt.txt", line_list[0])
    print(line_list)
    line_list = []
    start = 0
    i += 1



# print(line_list)

    # create_file("/home/kplinux/projects/ocr/samples/label-samples/" + str(i) + ".gt.txt", line)
    # i = i + 1
    # if i == 1:
        # break

