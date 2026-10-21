class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Check if lengths are the same
            return False

        countS, countT = {}, {} #hashmap in python 
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #If key not there then default will be 0 for s
            countT[t[i]] = 1 + countT.get(t[i], 0) #If key not there then default will be 0 for t 
        for c in countS:
            if countS[c] != countT.get(c,0): # Use get if key isn't there to default to 0.
                return False

        return True 