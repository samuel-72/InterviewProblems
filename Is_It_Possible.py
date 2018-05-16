# Complete the function below.


def  isitpossible( a,  b,  c,  d):
    if ( a == c and b == d ):
        return "Yes"
    
    input = []
    input.append((a,b))
    
    while (input):
        X, Y = input.pop(0)
         
        
        if ( X == c and Y == d ):
            return "Yes"
        
        X_Sum_Y = X + Y
        
        if (X_Sum_Y <= c):
            input.append( (X_Sum_Y, Y) )
        if (X_Sum_Y <= d):
            input.append( (X,X_Sum_Y) )
            
    return "No"

print isitpossible(1,4,5,9)