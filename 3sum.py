class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        lst = []
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if(total) == 0:
                    lst.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    #while left < right and nums[right] == nums[right - 1]:
                        #right -= 1
                    left += 1
                    #right -= 1
                elif(nums[i]+nums[left]+nums[right]) < 0:
                    left += 1
                else:
                    right -= 1
        return lst