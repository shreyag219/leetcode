class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]   # best sum of subarray ending exactly at current index
        max_sum = nums[0]       # best sum seen across all indices so far
        
        for i in range(1, len(nums)):
            # Either extend the previous subarray, or start fresh at nums[i]
            current_sum = max(nums[i], current_sum + nums[i])
            # Update global best if current streak beats it
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        