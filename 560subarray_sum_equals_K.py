class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
           # Dictionary to store the frequency of prefix sums
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1 # Handle the case where a subarray starts from index 0

        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            
            # Check if (current_sum - k) has been seen before
            # If it has, it means we found a subarray that sums to k
            if (current_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]
            
            # Update the frequency of the current prefix sum
            prefix_sum_counts[current_sum] += 1
            
        return count