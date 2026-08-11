def self_divisible (n):
    temp = n
    while n > 0:
        digit = n % 10
        if digit == 0:
            return False
        if temp % digit != 0:
            
            return False
        n//=10
    return True

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lst = []
        for i in range (left,right+1,1):
            if self_divisible(i) == True:
                lst.append(i)
        return lst
        