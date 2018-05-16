# Complete the function below.


def  mystery( letter):
    
    
    
    for letter_of_i in letter:
        
        no_of_operations = 0
        list_of_characters = list(letter_of_i)
        
        if ( list_of_characters == list_of_characters[::-1] ):
            print no_of_operations
            continue
        
            
        else:
            while (list_of_characters):
                
                if ( len(list_of_characters) > 1 ):
                    no_of_operations += abs( ord(list_of_characters[0]) - ord(list_of_characters[-1]) )
                    list_of_characters.pop(0)
                    list_of_characters.pop(-1)
                    
                else:
                    list_of_characters.pop()
            
               
        print no_of_operations
                        

print mystery( [ 'abc', 'abcba', 'abcd' ] )