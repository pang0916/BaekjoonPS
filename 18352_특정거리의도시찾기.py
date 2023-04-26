from sys import stdin
from queue import deque
input = stdin.readline

def parse_input():
    node_size, edge_size, target_distance, starting_node = map(int, input().split())
    graph = [[] for _ in range(node_size + 1)]
    for i in range(edge_size):
        start, end = map(int, input().split())
        graph[start].append(end)
    
    return node_size, edge_size, target_distance, starting_node, graph

def main():
    node_size, edge_size, target_distance, starting_node, graph = parse_input()
    queue = deque()
    queue.append(starting_node)
    
    visited = [False] * (node_size + 1)
    visited[starting_node] = True
    distance = 0
    
    while distance != target_distance:
        for i in range(len(queue)):
            cur_node = queue.popleft()
            
            for near_node in graph[cur_node]:
                if not visited[near_node]:
                    visited[near_node] = True
                    queue.append(near_node)
        distance += 1
    
    if len(queue) == 0:
        print(-1)
    else:
        print("\n".join(map(str, sorted(list(queue)))))

if __name__ == "__main__":
    main()