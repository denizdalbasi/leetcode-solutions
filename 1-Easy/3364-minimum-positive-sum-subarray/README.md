# 3364. Minimum Positive Sum Subarray

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Unique Set Filtering | 50 ms   | 19.03 MB |

### Approach Analysis

After choosing a starting index, we run a second loop inside to expand the subarray and calculate its sum. We check whether the subarray is valid: its length is between l and r, inclusive, and its sum is greater than 0. The second condition checks whether we haven't found a valid sum yet (ans == -1), in which case we save the current sum. Otherwise, if we find a smaller positive sum (total < ans), we replace the current answer.
