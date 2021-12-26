class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[len(nums) - k :] + nums[:len(nums) - k]
        # if k>0:
        #     temp = nums[len(nums)-1]
        #     i = len(nums)-2
        #     while i>=0:
        #         nums[i+1] = nums[i]
        #         i-=1
        #     nums[0] = temp
        #     k-=1
        # if k>0:
        #     self.rotate(nums,k)
