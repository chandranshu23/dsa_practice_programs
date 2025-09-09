class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            current_max = max(num, current_max + num)
            
            if current_max > global_max:
                global_max = current_max
                
        return global_max