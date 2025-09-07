class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[count] = nums[r] 
                count += 1
        return count    