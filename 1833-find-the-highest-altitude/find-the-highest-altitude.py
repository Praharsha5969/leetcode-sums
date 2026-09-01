class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixlist = [0]
        sum = 0
        for i in range(len(gain)):
            sum+=gain[i]
            prefixlist.append(sum)
        return max(prefixlist)
        