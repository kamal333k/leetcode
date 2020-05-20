class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        st = ""
        if len(strs) > 0:
            for i in range(len(strs[0])):
                st += (strs[0])[i]
                count = 0
                for x in strs:
                    if x.startswith(st):
                        count += 1
                if(count != len(strs)):
                    st = st[:-1]
                    break
        return st