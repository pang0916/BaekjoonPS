# INF로 초기화가 시간 다 잡아먹음

####### 참고 엄청한 bottom-up #######
from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    INF = 99999999
    STARTPOINT = 0
    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for x in range(2**N)] for _ in range(N)]

    def find(cur, visited):
        if visited == (1 << N)-1:         # 목표 도달하면 리턴
            if graph[cur][STARTPOINT] == 0:
                return INF
            else:
                return graph[cur][STARTPOINT]
        
        if dp[cur][visited] != -1:
            return dp[cur][visited]
        
        min_dist = INF
        for x in range(1, N):
            if graph[cur][x] == 0:      # 갈 수 없으면 skip
                continue
            if visited & (1 << x):      # 이미 방문한 도시라면 skip
                continue
            
            min_dist = min(min_dist, find(x, visited + (1 << x)) + graph[cur][x])
        
        dp[cur][visited] = min_dist
        return dp[cur][visited]

    print(find(0, 1))

main()

################# 원래시도도 맞음 top-down ##################
def main2():
    N = int(input())
    INF = 99999999
    STARTPOINT = 0
    graph = [list(map(int, input().split())) for x in range(N)]
    dp = [[-1 for x in range(2**N)] for _ in range(N)]

    def find(cur, visited):
        if dp[cur][visited] != -1:
            return dp[cur][visited]
        
        binary = bin(visited)[2:]
        visit = []
        for i in range(len(binary)):
            if i == cur:
                continue
            if binary[len(binary) - 1 - i] == '1':
                visit.append(i)
        
        if len(visit) == 0:
            if graph[STARTPOINT][cur] == 0:
                return INF
            dp[cur][visited] = graph[STARTPOINT][cur]
            return dp[cur][visited]
        
        min_dist = INF
        for x in visit:
            if graph[x][cur] == 0:
                continue
            min_dist = min(min_dist, find(x, visited - 2**cur) + graph[x][cur])
        
        dp[cur][visited] = min_dist
        return dp[cur][visited]

    find(0, (2**N)-1)
    print(dp[0][(2**N)-1])