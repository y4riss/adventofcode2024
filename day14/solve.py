robots = []
from collections import defaultdict
with open("input.txt")as file:
    for line in file:
        l = line.strip()
        left,right = l.split(" ")
        x,y = left.split("=")[1].split(",")
        a,b = right.split("=")[1].split(",")
        robots.append([(int(x), int(y)) , (int(a) , int(b))])


def first_part():

    count = defaultdict(lambda :0)
    m = 101
    n = 103
    rep = 100
    for robot in robots:
        x = (m + robot[0][0] + robot[1][0] * rep) % m
        y = (n + robot[0][1] + robot[1][1] * rep) % n
        count[(x,y)]+=1

    top_left = 0
    top_right= 0
    bottom_left= 0
    bottom_right= 0
    mid_x  = m//2
    mid_y = n//2
    for x,y in count:
        c = count[(x,y)]
        if x < mid_x and y < mid_y:
            top_left+=c
        elif x < mid_x and y > mid_y:
            bottom_left+=c
        elif x > mid_x and y < mid_y:
            top_right+=c
        elif x > mid_x and y > mid_y:
            bottom_right+=c

    ans = top_left * top_right * bottom_left * bottom_right
    # grid = [['.' for _ in range(m)] for _ in range(n)]
    # for row in range(n):
    #     for col in range(m):
    #         if count[(col,row)]:
    #             grid[row][col] = count[(col,row)]
    # for g in grid:
    #     print(g)
    print(ans)

def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

