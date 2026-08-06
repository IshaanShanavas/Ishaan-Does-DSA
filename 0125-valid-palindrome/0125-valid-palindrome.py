class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_new = s.strip().lower()

        import re

        s_new = re.sub("[^a-zA-Z0-9]", "", s).lower()


        return s_new == s_new[::-1]
        