class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(": ")", "{": "}", "[": "]"}
        
        
        for ch in s:
            if ch in m:
                stack.append(m[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
                
        return not stack
            