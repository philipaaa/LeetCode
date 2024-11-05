class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = 0
        i=1
        cur_val = nums[0]
        for i in range(n):
            if nums[i]!= cur_val:
                nums[k+1]=nums[i]
                k+=1
                cur_val =nums[i]
        
        return k+1

            