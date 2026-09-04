class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        left = 0
        
        current_sum = 0
        for right in range(len(nums)):
            current_sum +=nums[right]
            
            while current_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)

                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length

        