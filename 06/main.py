import numpy as np
import re

example = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip()

with open("06/input.txt") as f:
    from_file = f.read()

input = np.array([
    [
        cell
        for cell in re.split('\\s+', line)
        if cell.strip() != ""
    ]
    for line in from_file.splitlines()
])

def process(arr):
    operator = arr[-1]
    values = arr[:-1].astype(int)
    if operator == "*":
        return values.prod()
    else:
        return values.sum()

output = np.apply_along_axis(
    process,
    0,
    input
).sum()

print(output)