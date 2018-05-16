import timeit

'''
Seive of Eratosthenes
'''

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