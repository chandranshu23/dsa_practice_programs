class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
 
        return -1
                