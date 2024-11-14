class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)

        for i in nums:
            if nums.count(i) > (l/2):
                return i
            
    """
    Runtime 
        5927ms
        Beats 5.16%

    Memory
        13.00 MB
        beats 55.04%
    """
        
        