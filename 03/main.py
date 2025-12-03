# example = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """.strip().splitlines()

with open("03/input.txt") as f:
    input = f.readlines()

total = 0
for bank in input:
    combos = [
        int(bank[i] + bank[j])
        for i in range(0, len(bank))
        for j in range(i + 1, len(bank))
    ]
    total += max(combos)

print(total)
