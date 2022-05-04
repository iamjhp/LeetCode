class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # let P be the longest common prefix and 
        # the list strs is sorted alphabetically: strs[0] <= strs[1] <= ... <= strs[200]
        # then we only need to check if P is in strs[0] and strs[200]  
        # because if P is in in strs[0] and strs[200] then P must also be in strs[1] ~ strs[200]
        # why? because list is sorted alphabetically
        
        # example
        # strs = ["aaab", "aaac", "aad", "aaaae"]
        # sorted = ['aaaae', 'aaab', 'aaac', 'aad']
        # we iteratively check if the letter of sorted[0] and sorted[-1]
        # 1. iteration:
        #  sorted[0][:1] == sorted[-1][:1] -> True -> P = "a"
        # 2. iteration:
        #  sorted[0][:2] == sorted[-1][:2] -> True -> P = "aa"
        # 3. iteration:
        #  sorted[0][:3] == sorted[-1][:3] -> False -> P = "aa" is the longtest prefix
        
        
        if len(strs) == 1:
            return strs[0]
        
        # min/max returns the first/last string that would appear in the list if the list were ordered alphabetically
        s_min = min(strs) # s_min would be "aaaae" in the above example
        s_max = max(strs) # s_max "aad"
        
        if len(s_min) == 0:
            return ""
        
        for i, char in enumerate(s_min):
            if char != s_max[i]:
                return s_min[:i]
        
        # prefix == s_min
        return s_min
            
        
        