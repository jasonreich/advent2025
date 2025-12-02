# example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# input = example.split(",")

with open("02/input.txt") as f:
    input = f.readlines()[0].split(",")

total = 0

for i in input:
    [start, end] = i.split('-')
    for j in range(int(start), int(end) + 1):
        id = str(j)
        id_size = len(id)
        for segment_size in range(1, id_size // 2 + 1):
            if id_size % segment_size == 0:
                candidate = id[0:segment_size] * (id_size // segment_size)
                if id == candidate:
                    total += j
                    break

print(total)