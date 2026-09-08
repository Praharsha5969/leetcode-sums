class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in range(1, len(nums) + 1):
            if num not in freq:
                res.append(num)

        return res
        