grid= []
with open("sample.txt")as file:
    for line in file:
        grid.append(list(line.strip()))

def first_part():

    LEAVE = 1
    OBSTACLE = 2
    POSSIBLE = 3        
    n = len(grid)
    m = len(grid[0])

    guard = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                guard = [i,j]
                grid[i][j] = 'X'
    
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    currentDirection = 0
    def in_bound(i,j):
        return i >=0 and i < n  and j >=0 and j < m

    def canMove(i, j):
        dx, dy = directions[currentDirection]
        next_i = i + dx
        next_j = j + dy
        if not in_bound(next_i,next_j):
            return LEAVE
        if grid[next_i][next_j] == '#':
            return OBSTACLE
        return POSSIBLE

    def move():
        dx, dy = directions[currentDirection]
        guard[0] += dx
        guard[1] += dy
        grid[guard[0]][guard[1]] = 'X'

    while True:
        c = canMove(guard[0],guard[1])
        if c == POSSIBLE:
            move()
        elif c == OBSTACLE:
            currentDirection = (currentDirection + 1) % 4
        else:
            break

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += grid[i][j] == 'X'
    print(ans)
            




        


def second_part():
    pass


n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()

