class Solution(object):

    def longestPalindrome(self, s):

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res
    def helper(self, s, l, r):

        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        str=s[l+1:r]
        return s[l + 1:r]

if __name__=="__main__":
    s="abcbaasdfasfadfadf"
    print(s[0:2])
    sol=Solution()
    print(sol.longestPalindrome(s))