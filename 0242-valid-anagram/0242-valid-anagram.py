class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
    
        d = {}
        
        for ch in s:
            d[ch] = 1 + d.get(ch, 0)
            
        for ch in t:
            if d.get(ch, 0) <= 0: 
                return False
            
            d[ch] -= 1
            
        
        return True
        