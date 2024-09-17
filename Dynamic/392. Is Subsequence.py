# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        i = 0
        for j in range(0, len(t)):
            print()
            if i < len(s) and t[j] == s[i]:
                i += 1
        return i == len(s)

# print(isSubsequence("b", "abc"))
