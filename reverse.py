class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle the sign of the input integer
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        # Handle the integer overflow condition
        if reversed_x > 2**31 - 1:
            return 0
        
        return sign * reversed_x