class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        nums_dict = {} # val -> idx
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[n] = i