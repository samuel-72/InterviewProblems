import math

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]
    
print [m(3) for m in multipliers()]

m = multipliers()

for m in multipliers():
    print m(5)


def Seive(num):
    
    nums = range(2,num)
    print nums
    
    for i in range(2,int(math.sqrt(num))+1):
        nums = filter( lambda x : x == i or x % i , nums )
        
    print nums
    
Seive(100)


nu = range(2,50)
nu2= []
j =-1
for i in range(2,10):
    j += 1
    nu2 = filter( lambda x : x == i or x % i, nu)

print "nu2",nu2
'''


def multipliers2():
  return lambda x : 3 * x 

#print multipliers2()

def Seive(num):
    
    nums = range(2,num)
    
    for i in range(2,int(math.sqrt(num))+1):
        nums = filter( lambda x : x == i or x % i, nums )
        
    print nums
    
Seive(100)

nums = range(2,100)
nums = filter( lambda x : x % 7 == 0, nums )
    
print nums

print map(lambda w: len(w), 'It is raining cats and dogs'.split())

for n in range(2, 10):
    for x in range(2, n):
        print n,x
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
            
print range(2,3)

def fib(n):
    
    a,b=0,1
    while (a<n):
        print a,
        a,b = b,a+b
        
fib(10)        
'''