from PIL.Image import enum
from scipy.spatial import ConvexHull
from matplotlib.path import Path

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
    for line in from_file.splitlines()
    for [x, y] in [line.split(',')]
]

hull = ConvexHull(input)
path_obj = Path(hull.points[hull.vertices])

areas = [
    (abs(y1-y0) + 1) * (abs(x1 - x0) + 1)
    for i, (x0, y0) in enumerate(input)
    for (x1, y1) in input[i+1:]
    if path_obj.contains_path(Path([
        (min(x0, x1), min(y0,y1)),
        (min(x0, x1), max(y0,y1)),
        (max(x0, x1), max(y0,y1)),
        (max(x0, x1), min(y0,y1)),
        (min(x0, x1), min(y0,y1)),
    ]))
]

print(max(areas))