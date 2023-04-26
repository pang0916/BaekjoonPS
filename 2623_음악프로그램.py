# gold3, class5, topological sort

import sys
input = sys.stdin.readline

singersSize, subPdSize = map(int, input().split())
nodes = [set() for _ in range(singersSize+1)]
nodes_count = [0]*(singersSize+1)
result = []

for _ in range(subPdSize):
    sequences = list(map(int, input().split()))
    for i in range(1, sequences[0]):
        if sequences[i+1] not in nodes[sequences[i]]:
            nodes_count[sequences[i+1]] += 1
        nodes[sequences[i]].add(sequences[i+1])

def find(node):
    result.append(node)
    nodes_count[node] = -1
    for i in nodes[node]:
        nodes_count[i] -= 1
        if nodes_count[i] == 0:
            find(i)

for i in range(1, singersSize+1):
    if nodes_count[i] == 0:
        find(i)
        
print("\n".join(map(str, result))) if sum(nodes_count)==-singersSize else print(0)