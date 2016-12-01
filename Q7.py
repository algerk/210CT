def prime(p,n=2):
    if p % n == 0:
        #if remainder is 0 it cant be a prime number
        return False
    if n > p**0.5:
        #if n is greater than the SR of that number then return true
        return True
    else:
        return(prime(p,n+1))
    #if its not false then its going to keep going up until it finds the SR
