g = []
moves = []
# up right down left
dirs = [(-1, 0) , (0, 1), (1,  0), (0, -1)]
char_moves = {
    "^" : 0,
    ">" : 1,
    "v" : 2,
    "<" : 3
}
with open("input.txt")as file:
    ok = 0
    for line in file:
        l = line.strip()
        if not l:
            ok = 1
            continue
        if ok:
            # parse moves
            curr = []
            for c in l:
                curr.append(dirs[char_moves[c]])
            moves.extend(curr)
        else:
            #parse grid
            g.append(list(l))

n = len(g)
m = len(g[0])

def in_bound(i, j):

    return i >= 0 and i < n and j >= 0 and j < m

def performMove(i, j, dx, dy):

    x, y = i , j
    while in_bound(i,j) and (g[i][j] == 'O' or g[i][j] == '@'):
        i += dx
        j += dy

    if in_bound(i,j) and g[i][j] == '.':
            # swap first and last obstacle
            g[x + dx][y + dy] , g[i][j] =  g[i][j] , g[x + dx][y +  dy]
            # swap guard position with next obstacle
            g[x][y] , g[x + dx][y + dy] = g[x + dx][y + dy] , g[x][y]
            # return new guard pos
            return x + dx, y + dy

    # couldnt move, return initial position
    return x , y

def first_part():

    x,y = 0,0

    for i in range(n):
        for j in range(m):
            if g[i][j] == '@':
                x,y = i , j
                break
    for dx, dy in moves:
        x, y = performMove(x , y, dx, dy)

    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'O':
                ans += (100 * i + j)
    print(ans)



def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

