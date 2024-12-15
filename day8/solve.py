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
            for j in range(0 , nb_antennas):
                if i == j:
                    continue
                x,y = arr[i]
                a,b = arr[j]
                d = (a - x , b - y)
                antinode_1 = (x - d[0],y-d[1])
                antinode_2 = (a + d[0],b+d[1])
                if in_bound(antinode_1):
                    result.add(antinode_1)
                if in_bound(antinode_2):
                    result.add(antinode_2)
    print(len(result))





def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

