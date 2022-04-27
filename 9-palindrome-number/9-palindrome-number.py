class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x > 9 and x % 10 == 0:
            return False
        
        if x > 0 and x < 10:
            return True
        
        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
            
        return True if (x == reversed_x or x == reversed_x // 10) else False