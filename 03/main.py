example = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip().splitlines()

with open("03/input.txt") as f:
    input = f.readlines()

total = 0
for bank in input:
    bank = bank.strip()
    
    places = [ '_' for i in range(0, len(bank))]

    output = [ '0' for i in range(0, 12) ]
    i = 0
    for c in range(0, 12):
        m = max(bank[i:len(bank) - 11 + c])
        i = min([
            j
            for j in range(i, len(bank) - 11 + c)
            if bank[j] == m
        ]) + 1
        places[i - 1] = '^'
        output[c] = m[0]

    total += int(str(''.join(output)))

print(total)
