# 1846. Maximum Element After Decreasing and Rearranging

| Language | Approach                      | Runtime | Memory   |
| :------- | :---------------------------- | :------ | :------- |
| Python   | Sorting and Greedy Adjustment | 36 ms   | 27.56 MB |

### Approach Analysis

The problem asks us to find the largest possible value for the last element in an array after modifying it under two main rules:

1. The first element must always be 1.
2. The difference between any two touching elements cannot be greater than 1.

To solve this easily, I first sorted the array from smallest to largest. This makes it simple to build up the numbers step-by-step.

Then, I went through the sorted list and applied the rules. I forced the first number to be 1. For every next number, I checked if it was too large compared to the previous one. If the gap between them was bigger than 1, I simply decreased the current number so that it was exactly 1 greater than the previous number. By keeping the numbers as large as the rules allow all the way to the end, the very last element naturally becomes the maximum possible value.
