class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            a, b = s[l].lower(), s[r].lower()
            
            if a.isalnum() and b.isalnum():
                if a != b: return False
                
                l = l + 1
                r = r - 1
            else:
                l = l + (not a.isalnum())
                r = r - (not b.isalnum())
                
        return True