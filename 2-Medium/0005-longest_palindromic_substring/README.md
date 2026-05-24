# 5. Longest Palindromic Substring

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Center | 243 ms | 19.4 MB |

### Approach Analysis
Instead of using a heavy dynamic programming table, I treated every character (and the gap between characters) as a potential center of a palindrome, and then push two pointers outward as long as the characters match.

* **Runtime:** 243 ms. I ran a loop through the string and checked for two types of palindromes at each step: odd-length ones centered at a single character `(i, i)` and even-length ones centered between two characters `(i, i + 1)`.