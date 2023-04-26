from sys import stdin
input = stdin.readline

N, bag_size = map(int, input().split())
dp = [0] * (bag_size + 1)

for i in range(N):
    weight, value, howmany = map(int, input().split())
    
    if weight > bag_size:
        continue
    
    count = 1
    while howmany > 0:
        if howmany < count:
            count = howmany
            
        for j in range(bag_size, weight*count-1, -1):
            dp[j] = max(dp[j], dp[j-weight*count]+value*count)
        howmany -= count
        count = count << 1

print(dp[bag_size])