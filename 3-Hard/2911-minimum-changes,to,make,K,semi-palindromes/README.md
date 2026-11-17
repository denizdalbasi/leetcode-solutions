# 3003. Maximize the Number of Partitions After Operations

| Language | Approach                                     | Runtime | Memory   |
| :------- | :------------------------------------------- | :------ | :------- |
| Python   | Bitmask Dynamic Programming with Memoization | 3032 ms | 19.44 MB |

### Approach Analysis

The code first calculates the minimum number of changes needed to make every possible substring a semi-palindrome. It does this by checking all valid divisors of each substring's length and comparing characters that should be mirrored in each group. If two mirrored characters are different, one change is needed. It saves the smallest number of changes for each substring in the cost array. Then, it divides the string into exactly k substrings. The dp array stores the minimum number of changes needed to divide the first i characters into j parts. It tries different positions to split the string and uses the previously calculated costs to find the best result. Finally, it returns dp[n][k], which represents the minimum total number of changes needed to make all k substrings semi-palindromes.
