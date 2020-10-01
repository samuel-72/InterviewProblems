def recTraversal(row,column,path,pathList):
    global n
    path += str(row) + ',' + str(column)
    
    if ( row == n-1 and column == n-1):
        pathList.append(path)
        return True
        
    if ( row > n-1 or column > n-1 ):
        return False
        
    else:
        recTraversal(row+1,column,path,pathList)
        recTraversal(row,column+1,path,pathList)        
    
n = int(input("Enter the n in nxn matrix : ")) +1

pathList = []

recTraversal(0,0,"",pathList)

print pathList

