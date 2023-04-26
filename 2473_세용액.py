from sys import stdin
input = stdin.readline

N = int(input())
liquids = sorted(list(map(int, input().split())))
MAX = 9999999999

def find(target, start, end):
    lower = start
    upper = end
    
    nearest_liquids = [MAX, 0, 0, 0]
    
    while(lower < upper):
        sum_of_liquids = target + liquids[lower] + liquids[upper]
        if sum_of_liquids == 0:
            return [0, target, liquids[lower], liquids[upper]]
        elif sum_of_liquids < 0:
            if -sum_of_liquids < nearest_liquids[0]:
                nearest_liquids = [-sum_of_liquids, target, liquids[lower], liquids[upper]]
            lower += 1
        else:
            if sum_of_liquids < nearest_liquids[0]:
                nearest_liquids = [sum_of_liquids, target, liquids[lower], liquids[upper]]
            upper -= 1
    
    return nearest_liquids

result = [MAX, 0, 0, 0]

for i in range(N-2):
    temp = find(liquids[i], i+1, N-1)
    if result[0] > temp[0]:
        result = temp
    if temp[0] == 0:
        break
    
print(*result[1:4])