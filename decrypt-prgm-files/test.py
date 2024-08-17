list = [1, 54, 2, 5]

def add(x, y):
    return x + y

new_list = [add(i, 5) for i in range(len(list))]

print(new_list)