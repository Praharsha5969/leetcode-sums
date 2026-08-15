class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxcount = 0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
                maxcount=max(count,maxcount)
            else :
                count = 0
        return maxcount+1


        


        