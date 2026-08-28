class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = 0

        
        for i in range(len(digits)):
            num = num * 10 + digits[i]

        
        result = num + 1

        
        digits = []

        
        while result > 0:
            digi = result % 10
            digits.insert(0, digi)
            result //= 10

        return digits


        