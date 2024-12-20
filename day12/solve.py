g = []
with open("input.txt")as file:
    for line in file:
        g.append(line.strip())
        

def first_part():
    
    visited = set()
    n = len(g)
    m = len(g[0])
    ans = 0

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    area = 0
    perimeter = 0
    def in_bound(i,j):
         return i >= 0 and i < n and j >=0 and j < m
    def explore(i, j, plant):
        nonlocal area, perimeter  
        if not in_bound(i,j):
            return
        if (i,j) in visited:
            return
        if g[i][j] != plant:
            return

        area +=1 
        perimeter+=4
        for x,y in directions:
            if in_bound(i+x,j+y) and g[i+x][j + y] == plant:
                perimeter-=1
        visited.add((i,j))
        for x,y in directions:
            explore(i + x, j + y, plant)


        

    for i in range(n):
        for j in range(m):
            if (i,j) in visited:
                continue
            explore(i, j, g[i][j])
            ans += (area * perimeter)
            area = 0
            perimeter = 0
    print(ans)


def second_part():
    """
    idea : counting corners
    a corner can be : 
        - top left
        - top right
        - bottom left
        - bottom right
        - inside corner

    top left : top and left free
    top right : top and right free
    bottom left : bottom and left free
    bottom right : bottom and right free
    inside corner : in a 2*2 matrix, 3 plants belong and one doesnt or 3 plants dont belong and one does

    for the non inside corners, i just need to check two clockwise directions are free
    top -> right -> bottom -> left

    for the inside corner:
        i need to check for a current cell , its neighbours (top, right, bottom , left)
        for each two neighbours, compute the diagonal, and see if is not the same plant.

        for example:
        X ?
        X X
        X

        im at bottom left, my neighbours are top and right, so next is top right, if its not the same plant then thats a corner
        to compute the next cell out of the neighbours :
            add the dirs vectors together
            (1,0) + (0,1) = (1,1)        
    """
   
    visited = set()
    n = len(g)
    m = len(g[0])
    ans = 0

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    area = 0
    perimeter = 0
    def in_bound(i,j):
         return i >= 0 and i < n and j >=0 and j < m

    def is_free(i, j, plant):
        return not in_bound(i, j) or g[i][j] != plant
    def explore(i, j, plant):
        nonlocal area, perimeter  
        if not in_bound(i,j):
            return
        if (i,j) in visited:
            return
        if g[i][j] != plant:
            return

        for k in range(4):
            x, y= directions[k]
            x2, y2 = directions[(k + 1) % 4]
            if is_free(i + x, j + y, plant)  and is_free(i + x2, j + y2, plant):
                perimeter+=1
            if not is_free(i + x, j + y, plant)  and not is_free(i + x2, j + y2, plant) and is_free(i + x + x2, j + y + y2, plant):
                perimeter+=1
            

        
        area +=1 
        visited.add((i,j))
        for x,y in directions:
            explore(i + x, j + y, plant)


        

    for i in range(n):
        for j in range(m):
            if (i,j) in visited:
                continue
            explore(i, j, g[i][j])
            ans += (area * perimeter)
            area = 0
            perimeter = 0
    print(ans)


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

# area : number of letters in a component
# perimeter : 2 * area + 2