from functools import lru_cache
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
    for line in from_file.splitlines()
    for parts in [line.split(": ")]
]

G = nx.DiGraph()

for (src, dsts) in input:
    for dst in dsts:
        G.add_edge(src, dst)

def count_paths(src, dst):
    @lru_cache()
    def dfs(current):
        if current == dst:
            return 1
        
        return sum([
            dfs(neighbor) for neighbor in G.successors(current)
        ])
    return dfs(src)

dac_out = count_paths("dac", "out")
ffs_dac = count_paths("fft", "dac")
svr_fft = count_paths("svr", "fft")
print(dac_out * ffs_dac * svr_fft)