g = []
with open("input.txt")as file:
    for line in file:
        # g.append(list(map(int,line.strip())))
        row = []
        for x in line.strip():
            if x == '.':
                row.append(-1)
            else:
                row.append(int(x))
        g.append(row)


def first_part():

    print(g)
    n = len(g)
    m = len(g[0])
    ans = 0

    # dfs, k is current height
    directions = [(1,0),(-1,0), (0,1),(0,-1)]
    def explore(i, j, k, visited):

        if not (i >= 0 and i < n and j >= 0 and j < m):
            return 0
        
        if (i,j) in visited:
            return 0
        if g[i][j] != k or k > 9:
            return 0

        visited.add((i,j))
        if g[i][j] == 9:
            return 1
        
        ans = 0
        for x,y in directions:
            ans += explore(i + x , j + y, k + 1, visited)
        return ans

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                visited = set()
                ans+=explore(i,j, 0, visited)
    print(ans)

def second_part():

    n = len(g)
    m = len(g[0])
    ans = 0

    # dfs, k is current height
    directions = [(1,0),(-1,0), (0,1),(0,-1)]
    def explore(i, j, k, visited):

        if not (i >= 0 and i < n and j >= 0 and j < m):
            return 0
        
        if (i,j) in visited:
            return 0
        if g[i][j] != k or k > 9:
            return 0

        if g[i][j] == 9:
            return 1
        
        ans = 0
        for x,y in directions:
            visited.add((i,j))
            ans += explore(i + x , j + y, k + 1, visited)
            visited.remove((i,j))
        return ans

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                visited = set()
                ans+=explore(i,j, 0, visited)
    print(ans)



option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

