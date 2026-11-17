
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for rem in range(d):
                        left = l + rem
                        right = l + rem + ((length - 1 - rem) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[l][r] = min(cost[l][r], changes)

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                for p in range(j - 1, i):
                    if i - p < 2:
                        continue

                    dp[i][j] = min(
                        dp[i][j],
                        dp[p][j - 1] + cost[p][i - 1]
                    )

        return dp[n][k]
