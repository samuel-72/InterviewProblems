import sys
import math
import random
import timeit
'''
PROJECT EULER - PROBLEM 1

sums = 0
for i in xrange(1000):
    if ( (i % 3 == 0) or (i % 5 == 0) ):
        sums += i
        
print sums
    
'''



'''
PROJECT EULER - PROBLEM 2


def fibo(n):
    
    a,b = 1,2
    sums = 0
    
    while(b < n):
        if (b % 2 == 0):
            sums += b
        a,b = b,a+b

    print a,b
    return sums
    
print (fibo(4000000))

#print (fibo(40))

'''


'''
PROJECT EULER - PROBLEM 3

Rabin-Miller is a fast probabilistic algorithm to determine primality of a given no

def rabinMiller(num):
    # Returns True if num is a prime number.
    print "\n\nGoing to check if ",num,"is prime."
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
    
def factors(n):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
                
a = 600851475143
print "a = ",a," type = ", type(a), "sqrt = ",math.sqrt(a)
f_a = sorted(factors(a),reverse=True)
print f_a,len(f_a)

start = time.time()
for factor in f_a:
    if factor != 1 and factor != a:
        print "\n\nThe factor choosen is : ",factor
        isPrime = rabinMiller(factor)
        if isPrime == True:
            lp = factor
            print "\n\nThe largest prime factor is : ",factor
            break
        else:
            print "\n\nThe factor : " ,factor, "is not prime. "
            continue

print "Largest prime factor is : ", lp
print "\nElapsed time : ",start-time.time()            
'''


'''
PROJECT EULER - PROBLEM 4


def checkPalindrome(number):
    pal = list(str(number))
    if (len(pal) <= 1):
        return True
    else:
        while (pal):
            if (len(pal) <= 1):
                return True
            else:
                if (pal[0] == pal[-1]):
                    pal = pal[1:-1]
                    #print pal
                    if (len(pal) <= 1):
                        return True
                    continue
                else:
                    return False

max = 0

for no1 in range(999,99,-1):
    for no2 in range(990,99,-11):
        if ( checkPalindrome(no1*no2) ):
            #print "The palindrome of the product of two 3 digit nos " ,no1,no2, " is : ", no1*no2
            if (no1*no2 > max):
                max = no1*no2
                l = [no1,no2]
        else:
            continue

print "The palindrome of the product of two 3 digit nos is : ", max
print "The two nos are : ", l
'''


'''
PROJECT EULER - PROBLEM 5

2*3*5*7*11*13*17*19 = 9699690




def factors(n):
    return list(reduce(list.__add__ , ( [i] for i in range(1,21) if n % i == 0 ) ))

i = 0        
noList = []
for i in range(1,21):
    noList.append(i)


while(1):
    i += 9699690
    #print "Value of i in this iteration : ", i
    factorList = sorted(factors(i))
    if noList == factorList:
        print "The smallest no that is divisible by all numbers from 1 to 20 is : ", i
        break
    
'''



'''
PROJECT EULER - PROBLEM 6


When m = 10, n = 2
The Series = 1^n + 2^n + 3^n + .... + m^n 
Sum of the above series = ( m * (m+1) * (2m+1) ) / 6




def sumOfSquares(m):
    return ( ( m * (m+1) * (2*m+1) ) / 6.0 )
    
def squareOfSum(highLimit):
    s = 0
    for i in range(1,highLimit):
        s += i
    return ( (s**2) + (highLimit**2) + 2*s*highLimit )

print ( squareOfSum(10) - sumOfSquares(10)  )    
print ( squareOfSum(100) - sumOfSquares(100) )

'''



'''
PROJECT EULER - PROBLEM 6

def seive(n):
    
    if n <= 1:
        return []
    
    isComposite = [False] * (n+1)
    
    for i in range(3, int(n**0.5) + 1, 2):
        for j in range(3, n//i + 1, 2):
            isComposite[i*j] = True
            
    return [2] + [i for i in range(3, n, 2) if isComposite[i] == False]

    
start = timeit.default_timer()

#print len(seive(106000))    
print (seive(106000))[10000]

print "Total time taken : ", timeit.default_timer() - start

'''

#l = []

def biggestProduct(noOfAdjacentDigits,num):
    #global l
    
    maxProd = 1
    
    while(num):
        #t = []
        prod = 1
        
        for no in num[0:noOfAdjacentDigits]:
            prod *= int(no)     
            #t.append(no)
            
        if prod > maxProd:
            maxProd = prod
            #l = t

        num = num[1:]
    
    return maxProd
    
start = timeit.default_timer()
    
num = list(str("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"))    

print biggestProduct(13,num)
#print l
print "Total time taken : ", timeit.default_timer() - start
