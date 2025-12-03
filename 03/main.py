example = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip().splitlines()

with open("03/input.txt") as f:
    input = f.readlines()

total = 0
for bank in [input[0]]:
    output = list("000000000000")
    i = 0
    for c in range(0, 12):
        m = max(bank[i:len(bank) - 11 + c])
        i = min([
            j
            for j in range(i, len(bank) - 11 + c)
            if bank[j] == m
        ]) + 1
        output[c] = m[0]

    total += int(str(''.join(output)))

print(total)
