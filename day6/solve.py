from time import time
grid= []
with open("input.txt")as file:
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
     # idea : try every possible position as obstacle

    LEAVE = 1
    OBSTACLE = 2
    POSSIBLE = 3        
    n = len(grid)
    m = len(grid[0])

    guard = None
    initial_guard_pos = None
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                guard = [i,j]
    initial_guard_pos = guard.copy()
    
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    def in_bound(i,j):
        return i >=0 and i < n  and j >=0 and j < m

    def canMove(i, j, currentDirection):
        dx, dy = directions[currentDirection]
        next_i = i + dx
        next_j = j + dy
        if not in_bound(next_i,next_j):
            return LEAVE
        if grid[next_i][next_j] == '#':
            return OBSTACLE
        return POSSIBLE

    def move(guard, currentDirection):
        dx, dy = directions[currentDirection]
        guard[0] += dx
        guard[1] += dy
        return guard

    def isLoop():
        currentDirection = 0
        guard = initial_guard_pos.copy()
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        exhausted = 0
        while True:

            i = guard[0]
            j = guard[1]

            # if guard visited same position with same direction twice
            if visited[i][j] == currentDirection:
                return 1

            c = canMove(i, j, currentDirection)
            if c == POSSIBLE:
                visited[i][j] = currentDirection
                exhausted = 0
                guard = move(guard, currentDirection)
            elif c == OBSTACLE:
                currentDirection = (currentDirection + 1) % 4
                exhausted +=1
                if exhausted > 3:
                    return 1
            else:
                return 0

    start = time()
    for i in range(n):
        for j in range(m):
            if i == initial_guard_pos[0] and j == initial_guard_pos[1] or grid[i][j] == '#':
                continue
            grid[i][j] = '#'
            ans += isLoop()
            grid[i][j] = '.'

    end = time()
    print(f"time took : {end - start} ms")
    print(ans)
    

        


n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()

