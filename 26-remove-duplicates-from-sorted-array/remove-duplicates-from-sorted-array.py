class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = sorted(set(nums))

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)
        