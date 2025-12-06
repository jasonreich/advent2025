import numpy as np
import re

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

with open("06/input.txt") as f:
    from_file = f.read()

input = np.array([
    [
        cell
        for cell in line
    ]
    for line in from_file.splitlines()
]).transpose()

(rows, cols) = input.shape

operator = ''
acc = 0
total = 0
for i in range(0, rows):
    row = input[i]
    if row[-1].strip() != '':
        operator = row[-1]
        if operator == '*':
            acc = 1
        elif operator == '+':
            acc = 0
    
    value = ''.join(row[0:-1]).strip()
    if value != '':
        if operator == '*':
            acc *= int(value)
        elif operator == '+':
            acc += int(value)
    else:
        total += acc

total += acc
print(total)

# def process(arr):
#     operator = arr[-1]
#     values = arr[:-1].astype(int)
#     if operator == "*":
#         return values.prod()
#     else:
#         return values.sum()

# output = np.apply_along_axis(
#     process,
#     0,
#     input
# ).sum()

# print(output)