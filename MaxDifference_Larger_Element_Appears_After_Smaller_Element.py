def maxDiff(a):
    maxDiff = a[1] - a[0]
    # If larger no appears before smaller no then use below :
    # maxDiff = a[0] - a[1]
    minElt = a[0]
    for i in xrange(1,len(a)):
        if a[i] < minElt :
            minElt = a[i]
        if (a[i] - minElt > maxDiff):
            maxDiff = a[i] - minElt

    print "Maximum Difference : ",  maxDiff
    
maxDiff( [ 100,1,57,23,4,110,70,5,5,5,5,1 ] )