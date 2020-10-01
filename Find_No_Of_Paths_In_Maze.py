def recursiveTraversal(row,col):

    global n, path
    
    if ( row == n and col == n ):
        path += 1
        return True
            
    if ( row > n or col > n ):
        return False
    
    recursiveTraversal(row+1,col)
    recursiveTraversal(row,col+1)
    
n = int(input("Enter the n in NxN matrix : ")) 

path = 0

recursiveTraversal(0,0)

print "Total No of paths : " + str(path)
