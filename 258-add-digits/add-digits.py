class Solution:
    def addDigits(self, num: int) :
        s = 0
        while num:
            r = num %10
            s+=r
            num = num//10
            if s > 9 and num== 0:
                num = s
                s=0
        return s
        