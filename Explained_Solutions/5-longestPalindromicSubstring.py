# This can be done using a left and right pointer, and expanding around the center
# We have to account for the palindrome being even or odd length
# We first run through the string with the left and right pointer at the same index, and then expanding outwards, which would give us the odd length palindromes
# Then we run through the string with the left pointer at index i and the right pointer at index i + 1, and then expanding outwards, which would give us the even length palindromes
# We keep track of the longest palindrome found so far, and if we find a longer one, we update the longest palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.substring = ""
        self.length = 0

        for i in range(len(s)):
            # Odd length palindromes
            # left = right = i
            
            # While the left and right pointers are within bounds and the characters at those indices are equal
            # while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the length of the palindrome is greater than the current longest palindrome, update it
                # if right - left + 1 > length:
                #     substring = s[left:right + 1]
                #     length = right - left + 1
                # left -= 1
                # right += 1

            self.checkLongestPalindrome(s, i, i)  # Odd length palindromes

            # Even length palindromes
            # left= i, right = i + 1
            # While the left and right pointers are within bounds and the characters at those indices are equal
            # while left >= 0 and right < len(s) and s[left] == s[right]:
            #     # If the length of the palindrome is greater than the current longest palindrome, update it
            #     if right - left + 1 > length:
            #         substring = s[left:right + 1]
            #         length = right - left + 1
            #     left -= 1
            #     right += 1

            self.checkLongestPalindrome(s, i, i + 1)  # Even length palindromes

        return self.substring
    
    def checkLongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > self.length:
                self.substring = s[left:right + 1]
                self.length = right - left + 1
            left -= 1
            right += 1