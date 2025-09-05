class Solution(object):
    def twoSum(self, nums, target):
       mydict = {} #a hash map to store seen elements for constant lookup
       lst=[] #list to store out output
       for i,num in enumerate(nums):  #enum loop to get index and list element together
        complement = target - num  #other half of the two sum
        if complement in mydict:
            lst=[mydict[complement],i]  #preparing output
            return lst
        mydict[num]=i  # if we dont get wanted digits add to dict and move to next iteratiton
       
 
        