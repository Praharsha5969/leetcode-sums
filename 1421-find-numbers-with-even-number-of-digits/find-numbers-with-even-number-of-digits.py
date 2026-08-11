class Solution(object):
    def iseven(self,num):
        count = 0
        while num > 0:
            digit = num % 10
            count+=1
            num//=10
        return count % 2 == 0
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if self.iseven(nums[i]):
                count+=1
        return count
        