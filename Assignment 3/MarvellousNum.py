def ChkPrime(val):
    counter = 0
    for i in range(1,val+1):

        if val%i == 0:
            counter = counter + 1
    
    if counter == 2:
        return True
    else:
        return False