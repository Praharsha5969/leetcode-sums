class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans=[]
        for i in operations:
            if i=='+':
                ans.append(ans[-1]+ans[-2])
            elif i=='C':
                ans.pop()
            elif i=='D':
                a=ans[-1]
                ans.append(2*a)
            else:
                ans.append(int(i))
        return sum(ans)
        
        