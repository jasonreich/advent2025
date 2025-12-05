import re

example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()

with open("05/input.txt") as f:
    from_file = f.read()

[raw_intervals, ingredients] = [
    section.splitlines()
    for section in from_file.split('\n\n')
]

pattern = "([0-9]+)\\-([0-9]+)"

intervals = [
    range(int(match.group(1)), int(match.group(2)) + 1)
    for interval in raw_intervals
    if (match := re.search(pattern, interval))
]

count = 0
for ingredient in ingredients:
    if any(int(ingredient) in interval for interval in intervals):
        count+=1

print(count)