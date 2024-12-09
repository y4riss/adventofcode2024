data = []
with open("input.txt")as file:
    for line in file:
        x = map(int,line.strip().split(" "))
        data.append(list(x))
        


def first_part():
    
    ans = 0
    for row in data:
        n = len(row)

        increasing = 0
        decreasing = 0
        for i in range(1,n):
            c = row[i-1] - row[i]

            if abs(c) > 3 or c == 0:
                continue

            if c < 0:
                increasing+=1
            else:
                decreasing+=1
            if increasing >0 and decreasing>0:
                break
        if increasing == n-1 or decreasing==n-1:
            ans+=1
        else:
            ans+=0
    print(ans)

def second_part():
    pass






n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()
