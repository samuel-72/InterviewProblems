def smallest(n):
    parents = {}
    queue = [(1 % n, 1, None)]
    
    i = 0
    
    while i < len(queue):
        residue, digit, parent = queue[i]
        i += 1
    
        if residue in parents:
            continue
    
        if residue == 0:
            answer = []
    
            while True:
                answer.append(str(digit))
    
                if parent is None:
                    answer.reverse()
                    return ''.join(answer)
                digit, parent = parents[parent]
    
        parents[residue] = (digit, parent)
    
        for digit in (0, 1):
            queue.append(((residue * 10 + digit) % n, digit, residue))
    
    return None
    
print smallest(1998)