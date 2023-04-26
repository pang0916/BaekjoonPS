from sys import stdin
input = stdin.readline

x1, y1, x2, y2 = map(int, input().split())
dot1, dot2 = (x1, y1), (x2, y2)
x3, y3, x4, y4 = map(int, input().split())
dot3, dot4 = (x3, y3), (x4, y4)

def findCross():
    denominator = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/denominator
    y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/denominator
    return x, y

def CCW(x, y, z):
    temp = (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])
    if temp > 0: return 1
    elif temp == 0: return 0
    else: return -1

a = CCW(dot1, dot2, dot3)
b = CCW(dot1, dot2, dot4)

if a*b > 0:
    print(0)
elif a*b < 0:
    c = CCW(dot3, dot4, dot1)
    d = CCW(dot3, dot4, dot2)
    if c*d < 0:
        print(1)
        print(*findCross())
    elif c*d > 0:
        print(0)
    else:
        idx = 1 if dot3[0] == dot4[0] else 0
        if c == 0:
            if (min(dot3[idx], dot4[idx]) <= dot1[idx]) and (dot1[idx] <= max(dot3[idx],dot4[idx])):
                print(1)
                print(*dot1)
            else:
                print(0)
        elif d == 0:
            if (min(dot3[idx], dot4[idx]) <= dot2[idx]) and (dot2[idx] <= max(dot3[idx],dot4[idx])):
                print(1)
                print(*dot2)
            else:
                print(0)
else:
    idx = 1 if dot1[0] == dot2[0] else 0
    if a==0 and b==0:
        if (min(dot3[idx], dot4[idx]) > max(dot1[idx],dot2[idx])) or (min(dot1[idx], dot2[idx]) > max(dot3[idx], dot4[idx])):
            print(0)
        else:
            print(1)
            if (min(dot3[idx], dot4[idx]) == max(dot1[idx],dot2[idx])) or (min(dot1[idx], dot2[idx]) == max(dot3[idx], dot4[idx])):
                if (dot1[idx]==dot3[idx]): print(*dot1)
                elif (dot1[idx]==dot4[idx]): print(*dot1)
                elif (dot2[idx]==dot3[idx]): print(*dot2)
                elif (dot2[idx]==dot4[idx]): print(*dot2)
    elif a==0:
        if (min(dot1[idx], dot2[idx]) <= dot3[idx]) and (dot3[idx] <= max(dot1[idx],dot2[idx])):
            print(1)
            print(*dot3)
        else:
            print(0)
    elif b==0:
        if (min(dot1[idx], dot2[idx]) <= dot4[idx]) and (dot4[idx] <= max(dot1[idx],dot2[idx])):
            print(1)
            print(*dot4)
        else:
            print(0)