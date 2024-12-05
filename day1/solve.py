
x = []
y = []
with open("input.txt")as file:
    for line in file:
        a,_,_,b= line.strip().split(" ")
        x.append(int(a))
        y.append(int(b))


def first_part():
    x.sort()
    y.sort()
    ans = 0
    for i in range(len(x)):
        ans += abs(x[i] - y[i])
    print(ans)




def second_part():

    freq_right = {}
    for elem in y:
        if elem in freq_right:
            freq_right[elem]+=1
        else:
            freq_right[elem] = 1
    ans = 0
    for elem in x:
        if elem in freq_right:
            ans += (elem * freq_right[elem])
    print(ans)


n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()
