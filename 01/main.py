# example = """
# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82
# """

with open("01/input.txt") as f:
    input = f.readlines()

dial = 50
count = 0

for i in input:
    d = i[0]
    v = int(i[1:])
    if i[0] == "L":
        dial-=v
    else:
        dial+=v
    count+= abs(dial // 100)
    dial = dial % 100
    
print(count)

