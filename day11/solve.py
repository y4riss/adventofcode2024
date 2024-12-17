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
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

