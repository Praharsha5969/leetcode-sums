class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_divisible = 0
        sum_notdivisible = 0
        for i in range (1,n+1,1) :
            if i % m == 0 :
                sum_divisible = i + sum_divisible
            else :
                sum_notdivisible = i + sum_notdivisible
        return sum_notdivisible - sum_divisible
        