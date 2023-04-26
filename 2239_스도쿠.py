from sys import stdin
input = stdin.readline

table = list(map(int, input().rstrip()))
for _ in range(8):
    table.extend(list(map(int, input().rstrip())))
flag = False

def make(num):
    if num >= 81:
        global flag
        flag = True
        return
    
    if table[num] != 0:
        return make(num+1)
    
    for i in range(1, 10):
        if isitokay(num, i):
            table[num] = i
            make(num+1)
            if flag:
                return
            table[num] = 0
    
def isitokay(num, target):
    for i in range(num%9, 81, 9):
        if table[i] == target:
            return False
    for i in range(9*(num//9), 9*(num//9)+9):
        if table[i] == target:
            return False
    for i in range(((num%9)//3)*3+((num//27)*27), ((num%9)//3)*3+((num//27)*27)+27, 9):
        if table[i] == target or table[i+1] == target or table[i+2] == target:
            return False
    return True

make(0)
for i in range(9):
    print("".join(map(str, table[i*9 : i*9+9])))