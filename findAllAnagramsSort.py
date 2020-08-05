def findAnagramSort(s, p):
    if len(p) > len(s):
        return []
    p = sorted(p)
    
    start = 0
    res = []
    for e in range(len(p)-1, len(s)):
        cur = sorted(s[start: e+1])
        print(cur)
        if cur == p:
            res.append(start)
        start += 1
    return res
print(findAnagramSort("cbaebabacd","abc"))
        
