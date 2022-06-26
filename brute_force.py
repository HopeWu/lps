class Solution:
    def lps(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        for i in range(1, n):
            j = 1
            # while s[i - j] and s[i + j]:
            while i - j > 0 and i + j < n:
                if s[i-j] == s[i+j]:
                    dp[i] += 1
                j += 1
        # return max(dp)
        # print(max(dp))

        _max = max(dp)
        _max_index = 0
        for i in range(n):
            if dp[i] == _max:
                _max_index = i

        result = s[_max_index - _max: _max_index + _max]
        print(result)



solve = Solution()
solve.lps("abcdcab")
solve.lps("abcdcba")
solve.lps("abcd")
solve.lps("abaadcd")
