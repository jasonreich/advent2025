import networkx as nx

example = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()

with open("11/input.txt") as f:
    from_file = f.read()


input = [
    (parts[0], parts[1].split(' '))
    for line in example.splitlines()
    for parts in [line.split(": ")]
]

G = nx.DiGraph()

for (src, dsts) in input:
    for dst in dsts:
        G.add_edge(src, dst)

def count_paths(src, dst):
    return sum([
        1 for path in nx.all_simple_paths(G, source=src, target=dst)
    ])


print(count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))