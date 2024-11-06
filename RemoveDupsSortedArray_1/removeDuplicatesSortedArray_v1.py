class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = 0
        i=1
        if n == 1:
            k = 1
            return k

        # for i in range(n-1):
        while i <= n-1:
            if nums[k] == nums[i]:
                i += 1
            else:
                nums[k+1] = nums[i]
                k+=1
                i+=1

        return k+1