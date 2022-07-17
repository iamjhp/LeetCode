class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        for ch in t:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1
            if freq.get(ch, 0) == 0:
                del freq[ch]
                
        return True
            