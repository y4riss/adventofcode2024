disk_map = None
with open("input.txt")as file:
    disk_map = list(map(int,file.readline().strip()))
        

def first_part():

    blocks= []
    is_file = True
    current_file = 0
    for digit in disk_map:

        if is_file:
            for _ in range(digit):
                blocks.append(current_file)
        else:
            for _ in range(digit):
                blocks.append('.')
            current_file+=1
        is_file = not is_file

    n = len(blocks)
    i = 0
    j = n - 1
    while i <= j:

        while blocks[i] != '.':
            i+=1
        if i >= j:
            break
        blocks[i] = blocks[j]
        blocks[j] = '.'
        j-=1
    ans = 0
    for idx, x in enumerate(blocks):
        if x == '.':
            break
        ans += (idx * x)
    print(ans)



def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

