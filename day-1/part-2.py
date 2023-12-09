import os
import re

# Get the path of the input file
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./input.txt")

f = open(path)
lines = f.readlines()

DIGIT_STRINGS = ["one", "two", "three",
                 "four", "five", "six", "seven", "eight", "nine"]
total = 0


def parse_digit(digit_string):
    if digit_string.isnumeric():
        return int(digit_string)
    else:
        return DIGIT_STRINGS.index(digit_string) + 1


def handle_line(line):
    # Regex to detect DIGIT_STRINGS in the line
    forwards_rgx = re.compile(
        r"(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)")
    m = forwards_rgx.findall(line)
    left = parse_digit(m[0])
    flipped_line = line[::-1]

    # this will fix the edge case of threeight or oneight
    backwards_rgx = re.compile(
        r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9)")
    m = backwards_rgx.findall(flipped_line)
    right = parse_digit(m[0][::-1])
    return left * 10 + right


for i in range(len(lines)):
    line = lines[i]
    # Regex to detect DIGIT_STRINGS in the line
    total += handle_line(line)

print(total)
