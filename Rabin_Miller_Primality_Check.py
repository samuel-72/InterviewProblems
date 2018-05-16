import random
import timeit

def rabinMiller(n):
    # Returns True if num is a prime number.
    
    if (n % 2 == 0):
        return False
        
    s = n-1
    t = 0
    
    while(s%2 == 0):
        s = s//2
        t += 1
        
    for trials in range(5):
        a = random.randrange(2, n - 1) 
        v = pow(a,s,n)
        
        if (v != 1):
            i = 0
            while( v != (n-1) ):
                if ( i == t-1 ):
                    return False
                
                else:
                    i += 1
                    v = ( v**2 ) % n
    return True

        
start = timeit.default_timer()
noOfPrimes = 2
i = 3
iters = 0
while(1):
    i += 2
    iters += 1
    if (rabinMiller(i)):
        noOfPrimes += 1
        if noOfPrimes == 10001:
            print "The 10001th prime is : ",i, "Found after iteration no : ",iters
            break

print "Total time taken : ", timeit.default_timer() - start

#print rabinMiller(1025)  
#print rabinMiller(107243)  
#print rabinMiller(19)  
