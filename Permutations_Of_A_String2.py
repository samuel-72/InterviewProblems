def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute2(s[:i] + s[i+1:]):
                res += [c + perm]

    return res
    
print permute2("abc")

#print set(permute2("abcd"))