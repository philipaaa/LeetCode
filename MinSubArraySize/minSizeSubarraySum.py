class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #set variables needed
        current_sum = 0
        minLen = float('inf')
        left = 0
        n = len(nums)

        
        
        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                minLen = min(minLen, right - left +1)
                current_sum -= nums[left]
                left+= 1
        
        return minLen if minLen != float('inf') else 0
        