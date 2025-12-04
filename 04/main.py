import numpy as np
from scipy import signal

example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

with open("04/input.txt") as f:
    from_file = f.read()

input = np.array([
    [
        1 if c == '@' else 0
        for c in line
    ]
    for line in from_file.splitlines()
])

conv = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

last_count = -1
count = 0
state = input


while last_count != count:
    last_count = count
    
    accessible = (signal.convolve2d(state, conv, mode = 'same') < 4 * state).astype(int)
    
    count += sum(sum(accessible))
    state = state - accessible.astype(int)

print(state)
print(count)