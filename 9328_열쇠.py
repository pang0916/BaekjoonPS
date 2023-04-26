from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(45000)
input = stdin.readline

def dfs(keys, doors, building, row, column):
    current = building[row][column]
    
    # wall
    if current == '*':
        return
    
    else:
        # set visited '*'
        building[row][column] = '*'
        
        # empty
        if current == '.':
            pass
            
        # key
        elif current in 'abcdefghijklmnopqrstuvwxyz':
            keys.add(current)
            if current.upper() in doors:
                for door_row, door_column in doors[current.upper()]:
                    # restore door
                    building[door_row][door_column] = current.upper()
                    dfs(keys, doors, building, door_row, door_column)
            
        # doors
        elif current in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # have key
            if current.lower() in keys:
                pass
            # don't have key
            else:
                if current in doors:
                    doors[current].append((row, column))
                else:
                    doors[current] = [(row, column)]
                return
        
        # document
        elif current == "$":
            global result
            result += 1
        
        if column < len(building[0]) - 1 and (building[row][column+1] != '*'):
            dfs(keys, doors, building, row, column+1)
        if 0 < column and (building[row][column-1] != '*'):
            dfs(keys, doors, building, row, column-1)
        if row < len(building) - 1 and (building[row+1][column] != '*'):
            dfs(keys, doors, building, row+1, column)
        if 0 < row and (building[row-1][column] != '*'):
            dfs(keys, doors, building, row-1, column)
            

def main():
    # input parsing
    row_size, column_size = map(int, input().split())
    building = [list(map(str, input().rstrip())) for _ in range(row_size)]
    keys = set(input().rstrip())
    unopened_doors = {}
    
    for column in range(column_size):
        if building[0][column] != '*':
            dfs(keys, unopened_doors, building, 0, column)
    for row in range(1, row_size - 1):
        if building[row][0] != '*':
            dfs(keys, unopened_doors, building, row, 0)
        if building[row][column_size-1] != '*':
            dfs(keys, unopened_doors, building, row, column_size - 1)
    for column in range(column_size):
        if building[row_size-1][column] != '*':
            dfs(keys, unopened_doors, building, row_size - 1, column)

if __name__ == "__main__":
    for i in range(int(input())):
        result = 0
        main()
        print(result)