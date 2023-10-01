class Solution(object):
    def isPalindrome(self, x):
        if x < 0:  # Negative numbers are not palindromes
            return False
        
        # Convert the integer to a string
        x_str = str(x)
        
        # Compare the string with its reverse
        return x_str == x_str[::-1]