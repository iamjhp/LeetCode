class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        
        for ch in s:
            if ch == "(":
                my_stack.append(")")
            elif ch == "{":
                my_stack.append("}")
            elif ch == "[":
                my_stack.append("]")
            else:
                if len(my_stack) == 0:
                    return False
                stack_item = my_stack.pop()
                
                if stack_item != ch:
                    return False
        return not my_stack
                
            