def digit_sum(n):
    curr_sum = 0
    while n > 0:
        digit = n % 10
        curr_sum+=digit
        n//=10
    return curr_sum
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range (1,num+1):
            if digit_sum(i) % 2 == 0:
                count+=1
        return count
        