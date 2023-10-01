class Solution(object):
    def isMatch(self, s, p):
        # Create a 2D dp table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Set the initial condition
        dp[0][0] = True

        # Fill in the first row of the dp table
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill in the rest of the dp table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]