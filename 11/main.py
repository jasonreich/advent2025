import networkx as nx

example = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()

with open("11/input.txt") as f:
    from_file = f.read()


input = [
    (parts[0], parts[1].split(' '))
    for line in from_file.splitlines()
    for parts in [line.split(": ")]
]

G = nx.DiGraph()

for (src, dsts) in input:
    for dst in dsts:
        G.add_edge(src, dst)

print(sum([
    1 for path in nx.all_simple_paths(G, source="you", target="out")
]))
