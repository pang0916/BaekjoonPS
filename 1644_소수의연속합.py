from sys import stdin
input = stdin.readline

def main():
    N = int(input())

    primes = [0]
    visited = [True, True] + [False] * (N-1)
    result = 0

    flag = True
    for i in range(2, N):
        if not visited[i]:
            if flag:
                primes.append(i+primes[-1])
            if i > N//2 + 1:
                flag = False
            for j in range(i*i, N+1, i):
                visited[j] = True
                
    if not visited[N]:
        result += 1
    
    i = len(primes) - 1
    j = i-2
    
    while j >= 0 and j < i:
        hap = primes[i] - primes[j]
        if hap == N:
            result += 1
            i -= 1
            j -= 1
        elif hap > N :
            i -= 1
        else:
            j -= 1
    
    print(result)

main()