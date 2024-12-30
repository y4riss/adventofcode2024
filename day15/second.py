import sys
from collections import deque, defaultdict


def solve():

	whole_input = sys.stdin.read()
	grid, moves = whole_input.split("\n\n")
	moves = "".join(moves.strip().split("\n"))
	g = list(map(list,grid.split("\n")))
	n = len(g)
	m = len(g[0])
	# up right down left
	dirs = [(-1, 0) , (0, 1), (1,  0), (0, -1)]
	char_moves = {
		"^" : 0,
		">" : 1,
		"v" : 2,
		"<" : 3
	}
	# transforming grid
	for i in range(n):
		for j in reversed(range(m)):
			if g[i][j] == '.':
				g[i].insert(j, '.')
			elif g[i][j] == '#':
				g[i].insert(j, '#')
			elif g[i][j] == 'O':
				g[i][j:j+1] = ['[', ']']
			elif g[i][j] == '@':
				x,y = i, 2*j
				g[i][j:j+1] = ['@', '.']
	for m in moves:


		dx , dy = dirs[char_moves[m]]
		i,j = x,y
		if m == '<' or m == '>':
			while g[i][j] != '#' and g[i][j] != '.':
				j+=dy
			if g[i][j] == '#':
				continue
			while g[i][j] != '@':
				g[i][j] = g[i][j - dy]
				j-=dy
			g[i][j] = '.'
			y+=dy
		else:
			q = deque([(x + dx, y)])
			coords = defaultdict(list)
			wall = False
			while q:
				i,j = q.pop()
				if g[i][j] == '#':
					wall = True
					break
				if g[i][j] == '[':
					q.extendleft([(i + dx , j)])
					q.extendleft([(i + dx , j + 1)])
					coords[i].append(j)
					coords[i].append(j + 1)
				elif g[i][j] == ']':
					q.extendleft([(i + dx , j)])
					q.extendleft([(i + dx , j - 1)])
					coords[i].append(j)
					coords[i].append(j - 1)
				elif g[i][j] == '.':
					coords[i].append(j)
			if wall:
				continue
			# reverse if going down
			for i in sorted(coords,reverse=(dx == 1)):
				for j in coords[i]:
					if j in coords[i - dx]:
						g[i][j] = g[i - dx][j]
					else:
						g[i][j] = '.'
			g[x][y] = '.'
			x += dx
			g[x][y] = '@'

	ans = 0
	for i in range(n):
		for j in range(2*n):
			if g[i][j] == '[':
				ans += (i * 100 + j)
	print(ans)


solve()
