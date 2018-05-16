
n = int(raw_input("Enter the number: "))
i = 1
while (True):
    #print int( "{0:b}".format(i) )
    i += 1
    if ( int( "{0:b}".format(i) ) % n == 0 ):
        print "The smallest zero one number that is divisible by ", n, " is : ", "{0:b}".format(i)
        break