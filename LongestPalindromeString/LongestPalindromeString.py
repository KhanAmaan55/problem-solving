# MY SOLUTION
"""
def checkPalindrome(S):
    if S[0] == S[len(S)-1]:
        if(len(S) > 2):
            return checkPalindrome(S[1:(len(S)-1)])
        else:
            return True
    else:
        return False

def longest_palindromic_substring(s):
    longest = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            subString = s[i:(j+1)]
            if len(subString) > len(longest) and s[i] == s[j] and checkPalindrome(subString):
                longest = subString
    return longest
"""

# OPTIMIZED SOLUTION
def longest_palindromic_substring(s: str) -> str:
    if len(s) <= 1:
        return s

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check for odd-length palindromes (single center)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Check for even-length palindromes (pair center)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

print(longest_palindromic_substring("abbaaba"))