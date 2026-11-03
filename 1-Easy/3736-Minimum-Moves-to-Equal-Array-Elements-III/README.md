# 3120. Find the Number of Special Characters I

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Unique Set Filtering | 2 ms    | 19.28 MB |

### Approach Analysis

Calculating the maximum element in the given list and then going through each element and calculate how many times you have to increase the number to make it equal to the maximum number. At each calculation, you add the total increase requirement for all numbers and return that number to make all elements equal to the max number.
