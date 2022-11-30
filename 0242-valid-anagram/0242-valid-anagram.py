class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars_S, chars_T = {}, {}
        
        
        for i in range(len(s)):
            chars_S[s[i]] = 1 + chars_S.get(s[i], 0)
            chars_T[t[i]] = 1 + chars_T.get(t[i], 0)
            
        return chars_S == chars_T