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
        i = 0
        j = 0
        #create a third list
        nums3 = []
        #while pointers are still inbound
        while (i != m and j != n):
            #compare and add smallest number
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else: 
                nums3.append(nums2[j])
                j += 1
        #add the rest of the list for whichever list still has values
        if i == m:
            nums3.extend(nums2[j:n])
        else: 
            nums3.extend(nums1[i:m])
        #copy elem of nums3 into original list
        for k in range(len(nums3)):
            nums1[k] = nums3[k]
        