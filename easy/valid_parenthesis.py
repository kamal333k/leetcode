class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)%2 != 0):
            return False
        dic = {}
        dic['('] = ')'
        dic['{'] = '}'
        dic['['] = ']'
        stack = []
        for i in range(len(s)):
            if s[i] in dic:
                stack.append(s[i])
            else:
                if len(stack) == 0 or dic[stack.pop()] != s[i] :
                    return False
                    
        return len(stack) == 0