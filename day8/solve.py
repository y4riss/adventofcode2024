from collections import defaultdict
g = []
with open("input.txt")as file:
    for line in file:
        g.append(list(line.strip()))
        

def first_part():

    antennas = defaultdict(list)
    n = len(g)
    m = len(g[0])
    for i in range(n):
        for j in range(m):
            if g[i][j]!= '.':
                antennas[g[i][j]].append((i,j))
    
    result = set()
    def in_bound(node):
        i,j = node 
        return i >=0 and i < n and j >=0 and j < m
    for a in antennas:

        arr = antennas[a]
        nb_antennas = len(arr)
        for i in range(nb_antennas - 1):
            for j in range(i + 1 , nb_antennas):
                d = (abs(arr[i][0] - arr[j][0]) , abs(arr[i][1] - arr[j][1]))
                x,y = arr[i]
                a,b = arr[j]
                antinode_1 = [0,0]
                antinode_2 = [0,0]
                if x <= a:
                    antinode_1[0] = x - d[0]
                    antinode_2[0] = a + d[0]
                else:
                    antinode_1[0] = x + d[0]
                    antinode_2[0] = a - d[0]
                if y <= b:
                    antinode_1[1] = y - d[1]
                    antinode_2[1] = b + d[1]
                else:
                    antinode_1[1] = y + d[1]
                    antinode_2[1] = b - d[1]
                if in_bound(antinode_1):
                    result.add(tuple(antinode_1))
                if in_bound(antinode_2):
                    result.add(tuple(antinode_2))
    print(len(result))





def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

