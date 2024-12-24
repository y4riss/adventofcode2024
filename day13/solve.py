machines = []
with open("input.txt")as file:
    machine = []
    counter = 0
    for line in file:
        l = line.strip()
        if l:
            left,right = l.split(",")
            if counter < 2:
                _, a = left.split("+")
                _, b = right.split("+")
                machine.append((int(a),int(b)))
            else:
                _, a = left.split("=")
                _, b = right.split("=")
                machine.append((int(a),int(b)))
            counter+=1
        else:
            machines.append(machine)
            machine =[]
            counter = 0


def first_part():

    ans = 0
    MAX_CONST =100000000000000000000000000000000
    # print(machines)

    def solve(machine, tokens, x, y, A_PRESSED, B_PRESSED, visited):

        print((x,y))
        if x == machine[2][0] and y == machine[2][1]:
            return tokens
        if x > machine[2][0] or y > machine[2][1]:
            return  MAX_CONST
        # if A_PRESSED > 100 or B_PRESSED > 100:
        #     return MAX_CONST
        if (x,y) in visited:
            return MAX_CONST

        visited.add((x,y))
        a = solve(machine, tokens + 3, x + machine[0][0], y + machine[0][1], A_PRESSED + 1, B_PRESSED, visited)
        b = solve(machine, tokens + 1, x + machine[1][0], y + machine[1][1], A_PRESSED ,B_PRESSED + 1, visited)
        return min(a,b)

    for machine in machines:

        tokens = solve(machine, 0, 0, 0, 0, 0, set())
        if tokens != MAX_CONST:
            ans += tokens
    print(ans)


def second_part():
    """
    math time:

    we need i and j such that :
    i * vector(a) + j * vector(b) = vector(c)
    - vector(a) is (x,y) of button a
    - vector(b) is (x,y) of button b
    - vector(c) is (x,y) of the prize.

    it's a simple linear equations system, we find i and j, and then check back if results equal to vector c

    """

    ans = 0
    OFFSET = 10000000000000
    for machine in machines:

        ax,ay = machine[0]
        bx,by = machine[1]
        px,py = machine[2]
        px+=OFFSET
        py+=OFFSET



        i = (px*by - py*bx) // (ax*by - ay*bx)
        j = (py - i*ay) // by
        if i * ax + j * bx == px and i * ay + j * by == py:
            ans += (3*i + j)
    print(ans)

option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

