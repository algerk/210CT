def binarys(array, hi, lo, num):
    begin = 0
    end = num

    while(begin < end):
        mid = int (begin + (end - begin) / 2)#finds the midpoint of given list

        if lo > array[mid] and hi > array[mid]:#compares each int to previous one
            begin = mid +1

        elif lo < array[mid] and hi < array[mid]:
            end = mid

        else:
            return True

    return False



array = [5,7,9,11,13,17]
num = 6 #no of int within array
lo = 18 #the two values that make up the interval
hi = 20
print(binarys(array,hi,lo,num))

