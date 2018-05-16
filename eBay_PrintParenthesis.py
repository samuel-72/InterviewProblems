def Paren(l,startPos):
    global gl
    lcp = l[:]
    i = startPos
    j = 0

    while(i<len(lcp) and j <= 1):
        
        if (i < len(lcp)-1 and lcp[i] == ')' and lcp[i+1] == '('):
            t = lcp[i]
            lcp[i] = lcp[i+1]
            lcp[i+1] = t
            i += 1
            #print "LCP : ",lcp
            if ( str(lcp) not in gl ):
                gl[str(lcp)] = 0
                
            #print "LCP : ",lcp,"GL : ",gl
            #print "GL : ",gl
            
        if (i == len(lcp)-1):
            i = 0
            j += 1
            
        i += 1

def ParenPrepare(n):
    
    s = ''
    for i in range(n*2):
        if ( i % 2 == 0 ):
            s += '('
        else:
            s += ')'
    return s
            
gl = {}
n = input("Enter the no of parenthesis : ")
l = list(ParenPrepare(n))
gl[str(l)] = 0

for j in range(1,len(l)-1,2):
    Paren(l,j)
    
for keys in gl.keys():
    print "POSSIBLE COMBINATION : ", str(keys).replace("'","").replace("[","").replace(",","").replace("]","")

