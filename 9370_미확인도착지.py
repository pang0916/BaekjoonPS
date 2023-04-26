from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def parse_input():
    node_size, edge_size, target_size = map(int, input().split())
    graph = [[] for _ in range(node_size+1)]
    
    start_node, smell_node1, smell_node2 = map(int, input().split())
    
    for i in range(edge_size):
        node1, node2, cost = map(int, input().split())
        if (node1 == smell_node1 and node2 == smell_node2) or (node1 == smell_node2 and node2 == smell_node1):
            cost -= 0.1
        graph[node1].append((cost, node2))
        graph[node2].append((cost, node1))
        
    targets = set()
    for i in range(target_size):
        targets.add(int(input()))
    
    return node_size, graph, targets, start_node, smell_node1, smell_node2

def main():
    node_size, graph, targets, start_node, smell_node1, smell_node2 = parse_input()
    result = []
    
    heap = [(0, start_node)]
    costs = [int(1e9) for _ in range(node_size + 1)]
    costs[start_node] = 0
    visited = [False] * (node_size + 1)
    issmell = [False] * (node_size + 1)

    while len(targets) > 0 and heap:
        cur_cost, cur_node = heappop(heap)
        
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        
        if cur_node in targets:
            if issmell[cur_node]:
                result.append(cur_node)
            targets.remove(cur_node)
            
        for next_edge in graph[cur_node]:
            next_cost, next_node = next_edge
            if not visited[next_node] and (costs[cur_node] + next_cost < costs[next_node]):
                costs[next_node] = costs[cur_node] + next_cost
                
                issmell[next_node] = issmell[cur_node]
                if (cur_node == smell_node1 and next_node == smell_node2) or (cur_node == smell_node2 and next_node == smell_node1):
                    issmell[next_node] = True
                    
                heappush(heap, (costs[next_node], next_node))
    
    result.sort()
    print(*result)

if __name__ == "__main__":
    Testcase = int(input())
    for _ in range(Testcase):
        main()