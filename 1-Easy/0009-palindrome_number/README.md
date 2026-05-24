# 9. Palindrome Number

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Two-Pointer Array Comparison | 15 ms | 19.2 MB |

### Approach Analysis
Since negative numbers have a minus sign at the front, they can never be palindromes, so I instantly filtered them out. For positive numbers, I broke the integer down into a list of single digits. Then, I set up a pointer at the beginning (`left`) and another at the end (`right`), moving them inward to check if the numbers mirrored each other perfectly.

* **Runtime:** 15 ms. Converting the number to a string list takes a quick linear pass, and the two-pointer loop cuts the actual character comparisons in half by stopping right in the middle. It runs fast and keeps the logic completely straightforward.