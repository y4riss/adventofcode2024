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

    #00...111...2...333.44.5555.6666.777.888899
    #[2,3]  [12,3] [x,1] [x,1]...
    #[9,2] , [8,4] , [7,3]...

    # space = [starting_index, length]
    # elements = [starting_index, length]
    blocks= []
    is_file = True
    current_file = 0
    spaces = []
    files = []
    idx = 0
    for digit in disk_map:

        if is_file:
            files.append((idx, digit))
            idx+=digit
            for _ in range(digit):
                blocks.append(current_file)
        else:
            spaces.append([idx, digit])
            idx+=digit
            for _ in range(digit):
                blocks.append('.')
            current_file+=1
        is_file = not is_file

    n = len(files)
    i = n - 1

    # go through files from right to left
    while i >= 0:

        file_idx, file_size = files[i]
        curr_file = blocks[file_idx]



        # check all available spaces from left to right
        for j in range(len(spaces)):

            idx, length = spaces[j]

            # if space is available and file is actually in the right and spaces on left, fill space
            if length >= file_size and file_idx > idx:
                # fill from idx to idx+length with curr_file, and from file_idx to file_idx+file_size with dots
                for k in range(file_size):
                    blocks[idx + k] = curr_file
                    blocks[file_idx + k] = '.'
                
                # update space size with rest of space
                spaces[j][1] -= file_size
                # update where space starts
                spaces[j][0] += file_size
                break
        i-=1

    ans = 0
    for idx, x in enumerate(blocks):
        if x == '.':
            continue
        ans += (idx * x)
    print(ans)


   

            

  

option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

