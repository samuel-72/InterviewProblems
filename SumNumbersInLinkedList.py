#a = '879887651243985688880914'

#b = '871056341276812313549876'

a = '10100'
b = '910100'

l1 = []
l2 = []

for digit in a:
    l1.append(digit)
for digit in b:
    l2.append(digit)

print "No 1 : ",l1,"\nNo 2 : ",l2
ans = ''
s = []
q = 0

l_l1,l_l2 = len(l1)-1, len(l2)-1    

while(l_l1 >= 0 and l_l2 >= 0):
    print l_l1,l_l2

    if q > 0:
        su = q + int(l1[l_l1]) + int(l2[l_l2])
    else:
        su = int(l1[l_l1]) + int(l2[l_l2])

    if su > 9:
        s.append(su%10)
        q = su/10
    else:
        s.append(su)
        q = 0
    l_l1 -= 1
    l_l2 -= 1
    print s, l1[l_l1],l2[l_l2]
    
s2=s[:]
print s2,q, l_l1, l_l2 


if ( len(l1) < len(l2)):
    
    for i in range(l_l2,-1,-1):
        if q > 0:
            su = q + int(l2[i])
        else:
            su =  int(l2[i])

        if su > 9:
            s.append(su%10)
            q = su/10
        else:
            s.append(su)
            q = 0

    if (q > 0):
        s.append(q)       

elif ( len(l1) > len(l2)):
    
    for i in range(l_l1,-1,-1):
        if q > 0:
            su = q + int(l1[i]) 
        else:
            su = int(l1[i]) 

        if su > 9:
            s.append(su%10)
            q = su/10
        else:
            s.append(su)
            q = 0

    if (q > 0):
        s.append(q)  
    
elif (q > 0):
    s.append(q)       
        
for i in range(len(s)-1,-1,-1):
    ans += str(s[i])
    
print "Sum : ",ans
