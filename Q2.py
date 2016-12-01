def trlz(n):
    x = 1
    tList = []
    output = 0
    
    for i in range(2, n + 1):
        x *= i
    for i in str(x):
        tList.append(i)
    tList.reverse()
#iterates the factoral numbers, appends to list and then reversed
    for y in tList:
        if y == "0":
            output += 1
        elif y != 0:
            break
#goes through list and then counts 0's until it reaches a number >0
    return output



print(tList(34))



