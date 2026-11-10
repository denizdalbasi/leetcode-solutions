# 3693. Climbing Stairs II

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Shortest Path Search | 809 ms  | 33.40 MB |

### Approach Analysis

I used a DP array to store the minimum cost of reaching each step. For every step, I checked the previous one, two, and three steps to find the cheapest way to get there. I calculated the jumping cost and update the DP array if I find a lower cost. Finally, I returned dp[n], which gives me the minimum total cost to reach the last step.
