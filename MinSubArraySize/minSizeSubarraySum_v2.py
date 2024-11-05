class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minLen = float('inf')
        #set the prefix sum array
        prefix_sum = [0] * (n+1)

        #calculate the prefix sums
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        
