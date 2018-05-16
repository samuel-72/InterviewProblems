def checkPalindrome(s):
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == '(' and s[-1] == ')':
            return checkPalindrome(s[1:-1])
        else:
            return False
            

print checkPalindrome("((((a))")       
print checkPalindrome("(((())))")      
print checkPalindrome("((())))")      
print checkPalindrome("(()())")      