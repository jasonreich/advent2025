import enum
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

def matching_postions(match: str, lst: list[str]) -> set[int]:
    return set([
        i
        for i, v in enumerate(lst)
        if v == match
    ])

splits = 0
rays = set()
for row in input:
    splitters = matching_postions('^', row)
    hit = splitters.intersection(rays)
    
    splits += len(hit)
    rays.difference_update(hit)
    rays.update(map(lambda i: i-1, hit))
    rays.update(map(lambda i: i +1, hit))
    
    # Add Ses
    rays.update(matching_postions('S', row))
    
print(splits)