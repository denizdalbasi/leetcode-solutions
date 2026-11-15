# 1524. Number of Sub-arrays With Odd Sum

| Language | Approach                      | Runtime | Memory   |
| :------- | :---------------------------- | :------ | :------- |
| Python   | Sorting and Greedy Adjustment | 60 ms   | 24.31 MB |

### Approach Analysis

We iterate through the elements of the array one by one. For each element, we add its value to prefix to calculate the current prefix sum.
Then, we check whether the current prefix sum is even or odd.

- If the prefix sum is even, we add odd to result. This is because subtracting a previous odd prefix sum from the current even prefix sum gives us an odd subarray sum. After that, we increase even by 1 because we have found another even prefix sum.

- If the prefix sum is odd, we add even to result. This is because subtracting a previous even prefix sum from the current odd prefix sum gives us an odd subarray sum. After that, we increase odd by 1 because we have found another odd prefix sum.

We repeat this process until we have visited every element in the array.

Finally, we return result % MOD to make sure the answer does not exceed the required modulo value.
