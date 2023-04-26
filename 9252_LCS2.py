from sys import stdin
from bisect import bisect_right
input = stdin.readline

w1 = input().rstrip()
w2 = input().rstrip()
dp = [[0 for _ in range(len(w1)+1)] for __ in range(len(w2)+1)]

for j in range(1, len(w2)+1):
    for i in range(1, len(w1)+1):
        if w1[i-1] == w2[j-1]:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
            
result = []
row, column = len(dp)-1 , len(dp[0])-1
while dp[row][column] > 0:
    if w1[column-1] == w2[row-1]:
        result.append(w1[column-1])
        if dp[row][column] == 1:
            break
        row -= 1
        column -= 1
    elif dp[row-1][column] == dp[row][column]:
        row -= 1
    else:
        column -= 1
        
result.reverse()
print(len(result))
print("".join(result))