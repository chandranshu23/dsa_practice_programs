class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = []
        k=1
        for i in nums:
            j.append(k) 
            k = k*i
            
        l = 1
        for i in range(len(nums)-1,-1,-1):
            j[i] *= l
            l *= nums[i] 
        return j




        