example = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

with open("09/input.txt") as f:
    from_file = f.read()

input: list[tuple[int, int]] = [
    (int(x), int(y))
    for line in from_file.splitlines()
    for [x, y] in [line.split(',')]
]

areas = [
    (abs(y1-y0) + 1) * (abs(x1 - x0) + 1)
    for i, (x0, y0) in enumerate(input)
    for (x1, y1) in input[i+1:]
]

print(max(areas))