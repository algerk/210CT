import random
ulist = [5,3,8,6,1,9,2,7]
ulist2 = []

def rndList(n):
    for n in range(len(ulist)):
        #iterates the integers in the list
        x=random.randrange(len(ulist))
        #randomizes list
        ulist2.append(ulist[x])
        #appends to new list
        del ulist[x]

rndList(ulist)
print (ulist2)
        
    
