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

type coord = tuple[int, int]

input: list[coord] = [
    (int(x), int(y))
    for line in example.splitlines()
    for [x, y] in [line.split(',')]
]

hull: list[tuple[coord, coord]] = [
    ((min(x0, x1), min(y0, y1)), (max(x0, x1), max(y0, y1)))
    for i, (x0, y0) in enumerate(input)
    for (x1, y1) in input[i+1:]
    if x0 == x1 or y0 == y1
]

def is_in(x, y, hull) -> bool:
    return any([
        (x0 <= x <= x1) and (y0 <= y <= y1)
        for ((x0, y0), (x1, y1)) in hull
    ])

print('\n'.join([
    ''.join([
        'X' if is_in(x, y, hull) else '.'
        for x in range(0, 14)
    ])
    for y in range(0, 9)
]))

areas = [
    (abs(y1-y0) + 1) * (abs(x1 - x0) + 1)
    for i, (x0, y0) in enumerate(input)
    for (x1, y1) in input[i+1:]
]

print(max(areas))