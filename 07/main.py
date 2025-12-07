import numpy as np

example = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

with open("07/input.txt") as f:
    from_file = f.read()

input = from_file.splitlines()

rays = np.array([])
for row in input:
    if 'S' in row:
        rays = np.array([
            1 if c == 'S' else 0
            for c in row
        ])
    else:
        splitters = np.array([
            1 if c == '^' else 0
            for c in row
        ])
        
        next = np.convolve(
            splitters * rays, [1, 0, 1], 'same'
        )
        
        next += ((1 - splitters) * rays)
        
        rays = next
    
print(sum(rays))