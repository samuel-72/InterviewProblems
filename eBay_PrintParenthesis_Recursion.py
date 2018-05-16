s = '()()'

def par(s):
    
    if (s):
        for i in range(len(s)):
            return (  )
    else:
        return ''
        
def par2(s,start):
    
    if (s):
        for i in range(len(s)):
            return ( ')' + str(par( s[1:] )) )
            
    else:
        return ''
        
l = []                        
l.append(list(par(s)))
#l.append(list(par2(s)))

print l