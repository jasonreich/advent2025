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
    for line in example.splitlines()
    for [x, y] in [line.split(',')]
]

hull = ConvexHull(input)
path_obj = Path(hull.points[hull.vertices])

lower_x = min([ x for (x, _) in input ])
lower_y = min([ y for (_, y) in input ])
upper_x = max([ x for (x, _) in input ])
upper_y = max([ y for (_, y) in input ])

mid_x = (upper_x - lower_x) // 2
mid_y = (upper_y - lower_y) // 2

x0 = mid_x
x1 = mid_x
y0 = mid_y
y1 = mid_y

while True:
    if path_obj.contains_path(Path([(x0 - 1, y0), (x0 - 1, y1), (x1, y1), (x1, y0), (x0)])):
        x0 -= 1
    elif path_obj.contains_path(Path([(x0, y0 - 1), (x0, y1), (x1, y1), (x1, y0 - 1)])):
        y0 -= 1
    elif path_obj.contains_path(Path([(x0, y0), (x0, y1), (x1 + 1, y1), (x1 + 1, y0)])):
        x1 += 1
    elif path_obj.contains_path(Path([(x0, y0), (x0, y1 + 1), (x1, y1 + 1), (x1, y0)])):
        y1 += 1
    else:
        print((x0, y0), (x1, y1))
        print((abs(y1-y0) + 1) * (abs(x1 - x0) + 1))
        break
    

# areas = [
#     (abs(y1-y0) + 1) * (abs(x1 - x0) + 1)
#     for x0 in range(lower_x, upper_x + 1)
#     for y0 in range(lower_y, upper_y + 1)
#     if path_obj.contains_point((x0, y0))
#     for x1 in range(x0, upper_x + 1)
#     if path_obj.contains_point((x0, y0))
#     if path_obj.contains_point((x1, y0))
#     for y1 in range(y0, upper_y + 1)
#     if path_obj.contains_path(Path([
#         (x0, y0),
#         (x0, y1),
#         (x1, y1), 
#         (x1, y0)
#     ]))
# ]

# print(max(areas))