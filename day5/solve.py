rules = {}
updates = []
with open("input.txt")as file:

    get_rules = True
    for line in file:
        line = line.strip()
        if not line:
            get_rules = False
            continue
        if get_rules:
            a,b=line.split("|")
            if a in rules:
                rules[a].append(b)
            else:
                rules[a] = [b]
        else:
            updates.append(line.split(","))

        

def first_part():

    ans = 0
    for update in updates:
        
        good = True
        n = len(update)
        for i in range(n - 1):
            for j in range(i + 1 , n):
                if update[j] in rules and update[i] in rules[update[j]]:
                    good = False
                    break
        if good:
            ans += int(update[n//2])
    print(ans)

def second_part():

    ans = 0

    for update in updates:
        n = len(update)
        already_good = True
        while True:
            good = True
            for i in range(n - 1):
                for j in range(i + 1 , n):
                    if update[j] in rules and update[i] in rules[update[j]]:
                        good = False
                        already_good = False
                        update[i],update[j] = update[j],update[i]
            
            if already_good:
                break
            if good:
                ans += int(update[n//2])
                break
    print(ans)



n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()

