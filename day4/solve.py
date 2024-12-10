
grid = []
XMAS = "XMAS"
with open("input.txt")as file:
    for line in file:
        grid.append(line.strip())
        

def check(i,j, n , m):

    ans = 0
    if grid[i][j] != 'X':
        return 0
    
    # check XMAS forward
    if j + 3 < m:
        k = 1
        while k < 4 and grid[i][j + k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1

    # check XMAS backward (SAMX) 
    if j - 3 >= 0:
        k = 1
        while k < 4 and grid[i][j - k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1


    # check vertical down
    if i + 3 < n:
        k = 1
        while k < 4 and grid[i + k][j] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1
        
    # check vertical up
    if i - 3 >= 0:
        k = 1
        while k < 4 and grid[i - k][j] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1

    # check right diagonal down
    if i + 3 < n and j + 3 < m:
        k = 1
        while k < 4 and grid[i + k][j + k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1

    # check left diagonal down
    if i + 3 < n and j - 3 >= 0:
        k = 1
        while k < 4 and grid[i + k][j - k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1
        
    # check right diagonal up
    if i - 3 >= 0 and j + 3 < m:
        k = 1
        while k < 4 and grid[i - k][j + k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1

    # check left diagonal up
    if i - 3 >= 0 and j - 3 >=0:
        k = 1
        while k < 4 and grid[i - k][j - k] == XMAS[k]:
            k+=1
        if k == 4:
            ans +=1

    return ans



def first_part():


    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += check(i,j, n , m)
    print(ans)

def second_part():
    pass


n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()

