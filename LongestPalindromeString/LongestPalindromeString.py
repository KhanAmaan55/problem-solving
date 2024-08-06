# MY SOLUTION
"""
def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s
    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            subString = s[i:j+1]
            if len(subString) > len(longest) and subString == subString[::-1]:
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