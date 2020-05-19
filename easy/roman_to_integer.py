class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev = s[::-1]
        dist = {}
        dist['I'] = 1
        dist['V'] = 5
        dist['X'] = 10
        dist['L'] = 50
        dist['C'] = 100
        dist['D'] = 500
        dist['M'] = 1000
        
        i=0
        result = 0
        while  i < len(rev):
            res = 0
            res += dist[rev[i]]
            
            while (i+1 < len(rev) and (dist[rev[i+1]] < dist[rev[i]])):
                res -= dist[rev[i+1]]
                i+=1
            result += res
            i+=1
            
        return result