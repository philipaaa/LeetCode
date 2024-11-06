class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #set pointers
        k =0
        i=1
        repeated = False

        n = len(nums)

        while i <= n-1:
            if (nums[k] == nums[i]) and (repeated == True):
                i+=1
            elif (nums[k] == nums[i]) and (repeated == False):
                repeated = True
                nums[k+1] = nums[i]
                k+=1
                i+=1
            else: 
                nums[k+1] = nums[i]
                i+=1
                k+=1
                repeated = False

        return k+1


