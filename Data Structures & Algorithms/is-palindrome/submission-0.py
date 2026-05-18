class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s) - 1
        while x < y:
            while x < y and not s[x].isalnum():  # skip non-alphanumeric
                x += 1
            while x < y and not s[y].isalnum():  # skip non-alphanumeric
                y -= 1
            if s[x].lower() != s[y].lower():     # case insensitive compare
                return False
            x += 1
            y -= 1
        return True

            