class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq ={}
        for i in s:
            freq[i] = freq.get(i,0)+1
        res = []
        
        while freq:
            max_key = 0
            max_value = 0
            max_key = max(freq, key=freq.get)
            max_value = freq[max_key]
            for i in range(max_value):
                
                res.append(max_key)
            freq.pop(max_key)
            
            
        return "".join(res)
        
        
        