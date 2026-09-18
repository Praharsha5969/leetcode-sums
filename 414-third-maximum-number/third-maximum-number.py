class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        for i in range(2):
            s = max(nums)
            nums.remove(s)

        return max(nums)