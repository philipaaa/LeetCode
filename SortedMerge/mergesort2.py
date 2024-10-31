##This solution we will be more memory efficient by using the space in nums1
#we will go from back to front

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        'lets set some pointers'
        i = m-1
        j = n-1
        k = i+j+1
        #while pointers are still inbound
        while (i != -1 and j != -1):
            #compare and add largest number
            #to the end of the list 1
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else: 
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        #add the rest of the list for whichever list still has values
        if i == -1:
            while (j >= 0):
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        