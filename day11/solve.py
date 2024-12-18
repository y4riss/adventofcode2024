from collections import defaultdict
stones = []
with open("input.txt")as file:
    for line in file:
        line = line.strip()
        stones = line.split(" ")
        

def first_part():

    curr_stones = stones
    for _ in range(25):

        new_stones = []

        for stone in curr_stones:
            n = len(stone)
            if stone == '0':
                new_stones.append('1')
            elif n % 2 == 0:
                new_stones.append(stone[:n//2])
                new_stones.append(str(int(stone[n//2:])))
            else:
                new_stones.append(str(int(stone) * 2024))
        curr_stones = new_stones
        
    print(len(curr_stones))


def second_part():  

    """
    idea :
        Use two maps instead of two arrays
        go through each element in the map, where the key is the number, and the value is its occurence (frequency)

        check each condition, and update the map accordingly
        for example : [125, 17] would be
        {
            125 : 1
            17 : 1
        }
        new_map = {}
        new_map[125 * 2024]+=count
        new_map[1]+=count
        new_map[7]+=count

        where count is the number of times X appears
        for example if we had 1 1 1 1 1, instead of doing the same operation for 1, we could just say that m[2024]=5

        and finally get count of all elements in map
        this ensures that the array is not too big and elements are not repeated.
    """

    int_stones = list(map(int, stones))
    m = defaultdict(lambda : 0)
    for s in int_stones:
        m[s]+=1
    for _ in range(75):

        new_m = defaultdict(lambda : 0) 
        for stone, count in m.items():
            n = len(str(stone))
            if stone == 0:
               new_m[1]+=count
            elif n % 2 == 0:
                new_m[int(str(stone)[:n//2])]+=count
                new_m[int(str(stone)[n//2:])]+=count
            else:
                new_m[stone * 2024]+=count
        m = new_m
    ans = 0
    for x in new_m:
        ans += new_m[x]
    print(ans)


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

