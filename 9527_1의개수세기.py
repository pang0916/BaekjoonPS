from sys import stdin
input = stdin.readline

def find(N):
    count = 0
    N = str(bin(N))[2:]
    result = len(N)*(2**(len(N)-1))
    
    for index, i in enumerate(N):
        if i == "1":
            count += 1
        else:
            result -= (2**(len(N)-index-1))*(count+1) + ((2**(len(N)-index-1))//2)*(len(N)-1-index)
            
    return result
    
def main():
    A, B = map(int, input().split())
    print(find(B)-find(A-1))

main()