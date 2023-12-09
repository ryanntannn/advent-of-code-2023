import os

# Get the path of the input file
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./input.txt")

f = open(path)
lines = f.readlines()

total = 0

for i in range(len(lines)):
    line = lines[i]
    # Left pointer traverses from left to right
    l_ptr = 0
    l_val = -1
    while l_val < 0:
        if line[l_ptr].isnumeric():
            l_val = int(line[l_ptr])
        else:
            l_ptr += 1

    # Right pointer traverses from right to left
    r_ptr = len(line) - 1
    r_val = -1
    while r_val < 0:
        if line[r_ptr].isnumeric():
            r_val = int(line[r_ptr])
        else:
            r_ptr -= 1

    # Add sum to total
    total += l_val * 10 + r_val

print(total)
