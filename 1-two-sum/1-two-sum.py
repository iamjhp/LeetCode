class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [seen[remaining], i]
            
            seen[nums[i]] = i

            