# 3751. Total Waviness of Numbers in Range I

| Language | Approach          | Runtime | Memory    |
| :------- | :---------------- | :------ | :-------- |
| Python   | Relative Counting | 6874 ms | 165.34 MB |

### Approach Analysis

To find the path with the minimum bitwise XOR value from the top-left to the bottom-right, we need to explore all possible routes because XOR values can go up and down unlike normal addition. So I used a queue to move right and down step by step. At each step, I calculated the current XOR total and stored the state in a visited set so we don't repeat the same checks. Finally, when we reach the bottom-right corner, we compare all the results and return the smallest XOR value found.
