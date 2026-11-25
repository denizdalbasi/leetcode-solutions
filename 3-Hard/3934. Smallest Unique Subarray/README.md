# 3934. Smallest Unique Subarray

| Language | Approach                | Runtime | Memory   |
| :------- | :---------------------- | :------ | :------- |
| Python   | Greedy + Binary Lifting | 1241 ms | 45.30 MB |

### Approach Analysis

I calculated prefix hashes and powers of a fixed base. This allows us to get the hash of any subarray in constant time. I created a function called check(length) that calculates the hash of every subarray of a given length and stores its frequency in a dictionary. I check if any hash appears only once. If it does, the function returns True. Otherwise, it returns False. I used Binary Search to find the minimum valid length. If a unique subarray exists for one length, it will also exist for every larger length. When Binary Search finishes, lo contains the minimum length of a unique subarray, so I return it.
