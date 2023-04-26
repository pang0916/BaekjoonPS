from sys import stdin
input = stdin.readline

N = int(input())

dp = [[0, 0] for _ in range(N+1)]
matrixs = [()]

def find(start, count):
    if len(dp[start]) > count:
        return dp[start][count]
    
    largest = 199999999
    for i in range(1, count):
        plus = matrixs[start][0]*matrixs[start+i][0]*matrixs[start+count-1][1]
        largest = min(largest, find(start, i) + find(start+i, count - i) + plus)
        
    dp[start].append(largest)
    return largest

for i in range(N):
    row, column = map(int, input().split())
    matrixs.append((row, column))

print(find(1, N))