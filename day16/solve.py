import sys
import heapq

grid = sys.stdin.read().strip()
g = list(map(list, grid.split("\n")))

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# right down left up

def part1():
    n = len(g)
    m = len(g[0])

    # Find starting position
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'S':
                x, y = i, j
                break

    best = {}

    stack = []
    heapq.heappush(stack, (0, x,y, 0))

    while stack:
        score, i, j, direction= heapq.heappop(stack)
        if g[i][j] == 'E':
            print(score)
            return


        if (i, j, direction) in best and best[(i, j, direction)] <= score:
            continue

        best[(i, j, direction)] = score

        for k in range(4):
            dx, dy = dirs[k]
            ni, nj = i + dx, j + dy
            if ni < 0 or ni >= n or nj < 0 or nj >= m or g[ni][nj] == '#':
                continue
            new_score = score + (1 if k == direction else 1001)
            heapq.heappush(stack, (new_score, ni, nj, k))


part1()
