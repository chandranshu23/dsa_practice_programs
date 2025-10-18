class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        arr = list(zip(freq.keys(),freq.values()))
        arr.sort(key = lambda x:x[1], reverse = True)
        ans = []
        i = 0
        while i < k:
            ans.append(arr[i][0])
            i += 1

        return ans
        