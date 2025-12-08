from math import sqrt
from typing import Optional

example = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()

with open("08/input.txt") as f:
    from_file = f.read()

type coord = tuple[int, int, int]

input: list[coord] = [
    (x, y, z)
    for line in from_file.splitlines()
    for [x, y, z] in [map(int, line.split(','))]
]

with_distance: list[tuple[float, coord, coord]] = [
    (
        sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2) + pow(z0 - z1, 2)),
        (x0, y0, z0),
        (x1, y1, z1),
    )
    for i, (x0, y0, z0) in enumerate(input)
    for (x1, y1, z1) in input[i+1:]
]

with_distance.sort()

circuits: list[set[coord]] = []

for [d, c0, c1] in with_distance[0:1000]:
    if any(map(lambda circuit: c0 in circuit and c1 in circuit, circuits)):
        # Already connected
        pass
    else:
        c0_circuit: Optional[set[coord]] = next(filter(lambda circuit: c0 in circuit, circuits), None)
        c1_circuit: Optional[set[coord]] = next(filter(lambda circuit: c1 in circuit, circuits), None)
        
        if c0_circuit and not c1_circuit:
            c0_circuit.add(c1)
        elif not c0_circuit and c1_circuit:
            c1_circuit.add(c0)
        elif c0_circuit and c1_circuit:
            c0_circuit.update(c1_circuit)
            circuits.remove(c1_circuit)
        else:
            circuits.append(set([c0, c1]))
        

sizes = list(map(len, circuits))
sizes.sort(reverse=True)
print(sizes)
[l0, l1, l2] = sizes[0:3]
print(l0 * l1 * l2)