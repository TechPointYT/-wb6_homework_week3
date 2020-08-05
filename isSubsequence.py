class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
           return True 
        found = 0
        p1 = 0
        p2 = 0
        while p1 < len(t):
            if t[p1] == s[p2]:
                found += 1
                if p2 < len(s) - 1:
                    p2 += 1
            p1 += 1
        return  found == len(s)
