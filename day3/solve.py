all_data = [] 
with open("sample.txt")as file:
    for line in file:
        all_data.append(line.strip())
        

def first_part():


    ans = 0
    for data in all_data:
        n = len(data)
        i = 0
        while i < n:

            if i + 4 < n and data[i] == 'm' and data[i+1] == 'u' and data[i+2] == 'l' and data[i+3] == '(':
                i+=4
                a = 0
                while i < n and data[i].isnumeric():
                    a = a * 10 + int(data[i])
                    i+=1
                if i == n:
                    break
                if data[i] != ',':
                    continue
                i+=1
                b = 0
                while i < n and data[i].isnumeric():
                    b = b * 10 + int(data[i])
                    i+=1
                if i == n:
                    break
                if data[i] != ')':
                    continue
                ans += a*b
            i+=1
    print(ans)







def second_part():


    ans = 0
    compute = True
    for data in all_data:
        n = len(data)
        i = 0
        while i < n:

            if i + 4 < n  and data[i] == 'd' and data[i+1] == 'o' and data[i+2] == '(' and data[i+3] == ')':
                compute = True
                i+=4
                continue

            if i + 7 < n  and data[i] == 'd' and data[i+1] == 'o' and data[i+2] == 'n' and data[i+3] == '\'' and data[i+4] == 't' and data[i+5] == '(' and data[i+6] == ')':
                compute = False
                i+=7
                continue
            if compute and i + 4 < n and data[i] == 'm' and data[i+1] == 'u' and data[i+2] == 'l' and data[i+3] == '(':
                i+=4
                a = 0
                while i < n and data[i].isnumeric():
                    a = a * 10 + int(data[i])
                    i+=1
                if i == n:
                    break
                if data[i] != ',':
                    continue
                i+=1
                b = 0
                while i < n and data[i].isnumeric():
                    b = b * 10 + int(data[i])
                    i+=1
                if i == n:
                    break
                if data[i] != ')':
                    continue
                ans += a*b
            i+=1
    print(ans)



n = input("part ? > ")
if n == '1':
    first_part()
else:
    second_part()


