class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1       
        flag = False
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            middle = (left + right)//2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]
        