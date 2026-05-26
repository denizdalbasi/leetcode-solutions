# 3120. Find the Number of Special Characters I

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Unique Set Filtering | 0 ms | 19.35 MB |

### Approach Analysis

The straightforward way to handle this would be checking every single letter against the rest of the string, but nested loops quickly slow down performance. Instead, I used a hash set to strip away all duplicate characters instantly.

By converting the word into a `set()`, we reduce our search space to only unique letters. From there, we iterate through the set and look for valid pairs by applying two conditions:
1. Is the current character lowercase?
2. Does its uppercase equivalent exist in our unique set?

Checking **only** for lowercase characters is the trick here—it ensures we count each valid pair exactly once and prevents us from double-counting the pair when we eventually cross its uppercase version later in the loop.