# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Shortest Path Search | 0 ms    | 19.10 MB |

### Approach Analysis

We iterate through the array once and compare each element with the next one. If the next element is greater, we increase the increasing length and reset the decreasing length, and vice versa. If both elements are equal, we reset both lengths to 1 and update the longest length after each comparison. Finally, we return the longest length found
