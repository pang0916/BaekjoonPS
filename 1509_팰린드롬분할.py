from sys import stdin
input = stdin.readline

"""
팰린드롬 분할의 최소 갯수

BBCDDECAECBDABADDCEBACCCBDCAABDBADD : 22
QWERTYTREWQWERT : 5
"""

inputs = input().rstrip()
N = len(inputs)

# 팰린드롬 오른쪽 끝 인덱스에 왼쪽 끝 인덱스를 저장
palin_end = [[] for _ in range(N)]

if inputs[0] == inputs[1]:
    palin_end[1].append(0)
    
for i in range(2, N):
    # 짝수
    temp = 0
    while inputs[i-1-temp] == inputs[i+temp]:
        palin_end[i+temp].append(i-1-temp)
        temp += 1
        if i-1-temp < 0 or i+temp > N-1:
            break
    
    # 홀수
    temp = 0
    while inputs[i-2-temp] == inputs[i+temp]:
        palin_end[i+temp].append(i-2-temp)
        temp += 1
        if i-2-temp < 0 or i+temp > N-1:
            break

# DP 로 찾기
dp = [1 for x in range(N)]
for dp_count in range(1, N):
    # 바로 전 최솟값 + 1 로 초기화
    dp[dp_count] = dp[dp_count-1] + 1
    
    # palin_end 라면
    for palin_start in palin_end[dp_count]:
        if palin_start == 0:
            dp[dp_count] = 1
        else:
            dp[dp_count] = min(dp[dp_count], dp[palin_start-1]+1)
        
print(dp[-1])