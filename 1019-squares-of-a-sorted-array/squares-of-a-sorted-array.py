class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output =[]
        for i in range(0,len(nums)):
            output.append(nums[i]*nums[i])
        output.sort()
        return output
        