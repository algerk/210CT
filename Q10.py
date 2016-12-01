num=[1,2,5,4,1,2,1,4,5,6,7]

def maxlen(num):
    subsequence=[[]]#list to store any subsequences in ascending order found
    try:
        for n in range(len(num)):
            print(subsequence)
            if num[n] < num[n+1]:#if num[n]/next number is less than the next element, add to subsequence
                subsequence[-1].append(num[n])
            elif num[n] > num[n+1]:#if the sequence breaks, create new supsequnce and add to the end of new sequence
                subsequence[-1].append(num[n])
                subsequence.append([])
    except IndexError:#when it gets to the end of comparing elements, there will be an index error as n+1 is not available
        if num[-1] > num[-2]:#see's if next number fits into subsequence or not 
            subsequence[-1].append(num[-1])
        else:
            subequence.append([])
            subsequence[-1].append(num[-1])
            
    larsub=[]#stores and returns the longest subsequence found
    for i in subsequence:
        if len(i)>len(larsub):
            larsub=i
    return larsub

print(maxlen(num))
