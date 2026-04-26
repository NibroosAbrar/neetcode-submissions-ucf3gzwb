class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. lowercase the input
        2. check the character and ignores all non alphanumerics
        3. the inputs must be the same forward and backward
        """

        left = 0
        right = len(s)-1

        while left< right:
            if not s[left].lower().isalnum():
                left += 1
            elif not s[right].lower().isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True        