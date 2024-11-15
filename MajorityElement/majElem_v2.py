class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
    
    """
    Runtime
        0ms
        Beats 100%
    Memory
        12.93 MB
        Beats 64.34%
    """
    
