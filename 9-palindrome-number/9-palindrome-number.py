class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x > 9 and x % 10 == 0:
            return False
        
        if x > 0 and x < 10:
            return True
        
        reversed_x = 0
        copied_x = x
        while copied_x > 0:
            reversed_x = reversed_x * 10 + copied_x % 10
            copied_x = copied_x // 10
            
        return True if (x == reversed_x) else False