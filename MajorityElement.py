class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result, maxCount = 0,0
        for i in nums:
            count[i] = 1+count.get(i,0)
            if(count[i]>maxCount):
                result = i
            maxCount = max(count[i],maxCount)
        return result    
                
