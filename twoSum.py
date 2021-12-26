class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        TMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in TMap:
                return [TMap[diff],i]
            TMap[n]  = i
