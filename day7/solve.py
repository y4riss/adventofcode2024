equations = []
with open("input.txt")as file:
    for line in file:
        x = line.strip()
        value, numbers = x.split(":")
        numbers = numbers.strip().split(" ")
        numbers = list(map(int, numbers))
        equations.append([int(value), numbers])

def first_part():

    def generateOperations(i, n, arr, target, sum):

        if i == n:
            return sum == target

        return generateOperations(i+ 1, n, arr, target, sum + arr[i]) \
        or generateOperations(i+ 1, n,arr , target, sum * arr[i])

    ans = 0
    for eq in equations:
        val,numbers = eq
        if generateOperations(1, len(numbers),numbers, val, numbers[0]):
            ans += val
    print(ans)


def second_part():

    def generateOperations(i, n, arr, target, sum):

        if i == n:
            return sum == target

        return generateOperations(i+ 1, n, arr, target, sum + arr[i]) \
        or generateOperations(i+ 1, n,arr , target, sum * arr[i]) \
        or generateOperations(i+ 1, n,arr , target, int(f"{sum}{arr[i]}"))

    ans = 0
    for eq in equations:
        val,numbers = eq
        if generateOperations(1, len(numbers),numbers, val, numbers[0]):
            ans += val
    print(ans)



option = input("part ? > ")
if option == '1':
    first_part()
else:
    second_part()

