class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running = []
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            running.append(sum)
        return running
        