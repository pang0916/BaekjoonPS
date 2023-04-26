from sys import stdin
from collections import deque
input = stdin.readline

# Is two segment cross?
def isCross(dot1, dot2, dot3, dot4):
    x1,y1,_,x2,y2,_,x3,y3,_,x4,y4,_ = *dot1, *dot2, *dot3, *dot4
    cond01 = ((y2-y1)*(x3-x1)-(x2-x1)*(y3-y1))*((y2-y1)*(x4-x1)-(x2-x1)*(y4-y1)) <= 0
    cond02 = ((y4-y3)*(x1-x3)-(x4-x3)*(y1-y3))*((y4-y3)*(x2-x3)-(x4-x3)*(y2-y3)) <= 0

    if (((y1-y2)*(x2-x3) == (x1-x2)*(y2-y3))) and ((y2-y3)*(x3-x4) == (x2-x3)*(y3-y4)):
        if not (((max(x1, x2) < min(x3, x4)) or (min(x1, x2) > max(x3, x4))) or ((max(y1, y2) < min(y3, y4)) or (min(y1, y2) > max(y3, y4)))):
            # if dot[i]-dot[i+1] segment is included in root-last segment, don't change.
            if not (((max(x1, x2) <= max(x3, x4)) and (min(x1, x2) >= min(x3, x4))) or ((max(y1, y2) <= max(y3, y4)) and (min(y1, y2) >= min(y3, y4)))):
                if not (((max(x3, x4) <= max(x1, x2)) and (min(x3, x4) >= min(x3, x4))) or ((max(y3, y4) <= max(y1, y2)) and (min(y3, y4) >= min(y1, y2)))):
                    return 1
    elif cond01 and cond02:
        return 1
    return 0

def inputParser():
    inputarray = list(map(int, input().split()))
    dots = sorted([(inputarray[a*2+1], inputarray[a*2+2], a) for a in range(inputarray[0])])
    return dots
    
def main():
    dots = inputParser()
    
    # main segment : root-last
    root = dots[0]
    last = dots[-1]
    
    # add to deque straigt or reverse?
    forward = True
    answer = deque()
    
    for i in range(len(dots)-1):
        if forward:
            answer.append(dots[i][2])
        else:
            answer.appendleft(dots[i][2])
            
        if isCross(dots[i], dots[i+1], root, last):
            forward = not forward
            root = dots[i]
    
    answer.append(last[2])
    print(*list(answer))
        
N = int(input())
for _ in range(N):
    main()