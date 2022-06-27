class Solution:
    def lps(self, s: str) -> str:
        n = len(s)
        dp = [1]*n
        centers = [0]*n
        flag = [1]*n
        for i in range(1, n):
            _max = 0
            for j in range(i-1, int(i/2)):
                k = 1
                while j-k >= 0 and j+k < n:
                    if s[j-k] == s[j+k]

            dp[i] = max(dp[i-1], dp[i-1] + 1)


solve = Solution()
solve.lps("abcdcab")
solve.lps("abcdcba")
solve.lps("abcd")
solve.lps("abaadcd")
solve.lps("workattech")
solve.lps("workattaieng")
