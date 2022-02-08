class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while num > 0:
            ans += num % 10
            num = num // 10
            
            if num == 0 and ans > 9:
                num = ans
                ans = 0
        return ans