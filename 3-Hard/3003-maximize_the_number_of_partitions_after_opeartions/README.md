# 3003. Maximize the Number of Partitions After Operations

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Bitmask Dynamic Programming with Memoization | 1219 ms | 312.48 MB |

### Approach Analysis
I solved this problem by using dynamic programming to explore all possible choices of splitting the string and changing at most one character. Because we need to keep track of the letters we have seen so far, I used a binary number (bitmask) to remember them efficiently without taking up too much memory.

* **Tracking Characters:** As we go through the string letter by letter, we update our bitmask to remember which characters are in the current group.
* **Making the Change:** If we haven't changed a letter yet, we try changing the current letter to all 26 possible English letters to see which choice gives us the most splits.
* **Saving Time:** We save our results along the way so we don't do the same hard work twice, which keeps the program running smoothly.