class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0  # Variable to store the maximum length
        start = 0  # Start index of the current substring
        char_indices = {}  # Dictionary to store the last seen index of each character
        
        for i, char in enumerate(s):
            if char in char_indices and char_indices[char] >= start:
                # If the character is repeated within the current substring
                # Update the start index to the next position of the repeated character
                start = char_indices[char] + 1
            else:
                # Calculate the length of the current substring
                current_length = i - start + 1
                max_length = max(max_length, current_length)
            
            # Update the last seen index of the character
            char_indices[char] = i
        
        return max_length
