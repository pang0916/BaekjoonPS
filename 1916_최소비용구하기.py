from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def parse_input():
    node_size = int(input())
    edge_size = int(input())
    graph = [[] for _ in range(node_size + 1)]
    
    for i in range(edge_size):
        start, end, cost = map(int, input().split())
        graph[start].append((cost, end))
        
    '''
    graph : [[], [(COST, NEXT_NODE), (COST, NEXT_NODE)] , [(COST, NEXT_NODE)], ...]
    (index -> start node)
    '''
    
    target_start, target_end = map(int, input().split())
        
    return node_size, graph, target_start, target_end

def main():
    node_size, graph, target_start, target_end = parse_input()
    COST, NODE = 0, 1
    
    heap = []
    heap.append((0, target_start))
    visited = [False] * (node_size + 1)
    costs = [1999999999] *  (node_size + 1)
    costs[target_start] = 0
    
    while True:
        cur_edge = heappop(heap)
        visited[cur_edge[NODE]] = True
        
        if cur_edge[NODE] == target_end:
            print(cur_edge[COST])
            break
        else:
            for next_edge in graph[cur_edge[NODE]]:
                if not visited[next_edge[NODE]] and (costs[cur_edge[NODE]]+next_edge[COST] < costs[next_edge[NODE]]):
                    costs[next_edge[NODE]] = costs[cur_edge[NODE]]+next_edge[COST]
                    heappush(heap, (cur_edge[COST] + next_edge[COST], next_edge[NODE]))

if __name__ == "__main__":
    main()