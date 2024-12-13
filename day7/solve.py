equations = []
with open("input.txt")as file:
    for line in file:
        x = line.strip()
        value, numbers = x.split(":")
        numbers = numbers.strip().split(" ")
        numbers = list(map(int, numbers))
        equations.append([int(value), numbers])

        

def first_part():

    def generateOperations(level , n, arr, target, combin=[]):

        if level == n - 1:

            i = 1
            ans = arr[0]
            for op in combin:
                if op == "+":
                    ans += arr[i]
                else:
                    ans *= arr[i]
                i+=1
            return ans == target

        combin.append("+")
        x = generateOperations(level + 1, n, arr, target, combin)
        combin.pop()
        combin.append("*")
        y = generateOperations(level + 1, n,arr , target, combin)
        combin.pop()
        return x or y

    ans = 0
    for eq in equations:
        val,numbers = eq
        if generateOperations(0, len(numbers),numbers, val):
            ans += val
    print(ans)

def second_part():
    pass


option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

