size = 5 * 1000000 + 1
spf = [True] * size
spf[0] = spf[1] = False
i = 2
while i * i < size:
    if spf[i]:
        j = i*i
        while j < size:
            if spf[j] :
                spf[j] = False
            j += i
    i+=1
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1 :
            return 0
        count = 0
        for i in range(2,n):
            if spf[i]:
                count+=1
        return count
        
        

        