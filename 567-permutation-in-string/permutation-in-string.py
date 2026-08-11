class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1 = {}
        for i in s1 :
            d1[i] = d1.get(i,0) + 1
        d2 = {}
        left = 0
        flag = 0
        for right in range(len(s2)):
            d2[s2[right]] = d2.get(s2[right],0) + 1
            if right >= len(s1) - 1:
                if d1 == d2 :
                    flag = 1
                d2[s2[left]] -=1
                if d2[s2[left]] == 0:
                    d2.pop(s2[left])
                left+=1
        return flag == 1


        
        
        
        