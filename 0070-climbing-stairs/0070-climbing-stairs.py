class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        n1 = 3
        n2 = 2
        
        for i in range(4, n + 1) :
            tmp = n1 + n2
            n2 = n1
            n1 = tmp
            
        return n1
            