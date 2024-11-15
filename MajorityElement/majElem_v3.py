class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
    """
    Runtime
        0ms
        Beats 100%
    Memory
        12.79 MB
        Beats 88.94%
    """