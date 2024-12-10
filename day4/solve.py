
grid = []
XMAS = "XMAS"
with open("input.txt")as file:
    for line in file:
        grid.append(line.strip())
        

def check(i,j, n , m):

    ans = 0
    if grid[i][j] != 'X':
        return 0

    # forward, backward , up, down, diag down right, diag down left, diag up right, diag up left
    directions = [(0,1), (0, -1), (-1,0), (1,0), (1,1),(1,-1), (-1,1), (-1,-1)]
    def in_bound(x,y):
        return x >= 0 and x < n  and y >= 0 and y < m
    for dx,dy in directions:
        good = 1 
        for k in range(1,4):
            if not in_bound(i + dx * k , j + dy* k) or grid[i + dx * k][j + dy*k] != XMAS[k]:
                    good = 0 
                    break
        ans += good
    return ans


def check_2(i,j,n , m):

    MAS = 0
    if grid[i][j] != 'A':
        return 0
    
    if not (i - 1 >= 0 and j - 1 >= 0 and i + 1 < n and j + 1 < m):
        return 0

    """
    two possibilities :

    . . .
    . A .
    . . .

    
    either 
    M . .
    . A .
    . . S

    or 
    S . .
    . A .
    . . M

    and for each one , either :
    . . M
    . A .
    S . .

    or 
    . . S
    . A .
    M . .
    """


    # diagonal
    if grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' or grid[i - 1][j - 1] == 'S' and grid[i+1][j + 1] == 'M':
        MAS += 1
    
    if grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' or grid[i - 1][j + 1] == 'S' and grid[i  + 1][j - 1] == 'M':
        MAS += 1

    if MAS == 2:
        return 1 
    return 0
    
def first_part():


    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += check(i,j, n , m)
    print(ans)

def second_part():
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += check_2(i,j, n , m)
    print(ans)



n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()

