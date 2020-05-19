class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
#         res = 0;
#         if (-2**31) <= x <= (2**31 -1):
#             is_x_pos = 1 if x > 0 else -1
#             x = abs(x)
#             while x > 0 :
#                 res = 10*res + x%10
#                 x /= 10

#             res = is_x_pos * res
            
#         if (-2**31) <= res <= (2**31 -1):
#             return res
#         else:
#             return 0
        if (-2**31) <= x and x <= (2**31 -1):
            is_x_pos = 1 if x > 0 else -1
            rev = str(abs(x))
            res = int(rev[::-1])
            if (-2**31) <= res and res <= (2**31 -1):
                return res*is_x_pos
            else:
                return 0
        else:
            return 0
            