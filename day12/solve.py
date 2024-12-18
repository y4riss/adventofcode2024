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
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

# area : number of letters in a component
# perimeter : 2 * area + 2