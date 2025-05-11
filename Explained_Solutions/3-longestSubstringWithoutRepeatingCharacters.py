# Using a sliding window approach, you can keep track of the longest substring without repeating characters
# Initialize a set to keep track of duplicates
# Move the right pointer along the characters, if a duplicate is found then remove it from the set and move the left pointer towards the right

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Intialize the set to keep track of duplicates
        charSet = set()
        # Initialize the left pointer at index 0
        l = 0
        # Initalize inital length of longest substring to be 0
        length = 0

        # Keep moving the right pointer along the string s
        for r in range(len(s)):
            # While the character seen by the right pointer is in the set
            while s[r] in charSet:
                # Remove the character at the left pointer, which would be the duplicate of that seen by the right pointer
                charSet.remove(s[l])
                # Move the left pointer towards the right
                l += 1

            # Else add the current character seen by the right pointer to the set
            charSet.add(s[r])
            # Compare the maximum recorded length up until now and the current length of the substring being parsed
            length = max(length, r - l + 1)

        # Return the maximum length of substring 
        return length