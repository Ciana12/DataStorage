class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start = 0  # Start index of the longest palindromic substring
        end = 0  # End index of the longest palindromic substring
        
        for i in range(len(s)):
            # Check for palindromic substrings with odd length
            len1 = self.expandAroundCenter(s, i, i)
            # Check for palindromic substrings with even length
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # Find the length of the longest palindromic substring centered at index i
            length = max(len1, len2)
            
            # Update the start and end indices if a longer palindromic substring is found
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start:end+1]
    
    def expandAroundCenter(self, s, left, right):
        """
        Helper function to expand around a center and find the length of a palindromic substring.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1