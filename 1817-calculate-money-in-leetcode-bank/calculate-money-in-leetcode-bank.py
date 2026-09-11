class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        monday = 1

        while n > 0:
            for i in range(7):
                if n == 0:
                    break

                total += monday + i
                n -= 1

            monday += 1

        return total






        