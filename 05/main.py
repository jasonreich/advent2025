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
    (int(match.group(1)), int(match.group(2)))
    for interval in raw_intervals
    if (match := re.search(pattern, interval))
]

intervals.sort()

last_end = -1

count = 0

for (low, high) in intervals:
    actual_start = max(low, last_end + 1)
    
    if actual_start <= high:
        interval_count = high - actual_start + 1
        count += interval_count
        last_end = high
    
print(count)