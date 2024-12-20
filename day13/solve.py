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
    MAX_CONST =1000000000000000000000 

    def solve(machine, tokens, x, y, A_PRESSED, B_PRESSED, visited):

        if x == machine[2][0] and y == machine[2][1]:
            return tokens
        if x > machine[2][0] or y > machine[2][1]:
            return  MAX_CONST
        if A_PRESSED > 100 or B_PRESSED > 100:
            return MAX_CONST 
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
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

