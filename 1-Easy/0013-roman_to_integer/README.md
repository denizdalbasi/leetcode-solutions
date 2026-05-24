# 13. Roman to Integer

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Dictionary Scan | 4 ms | 19.4 MB |

### Approach Analysis
I used a dictionary to map each Roman numeral to its integer value. If a smaller numeral appears *before* a larger one, it means you subtract it (like `IV` for 4). I wrote a loop that looks ahead to the next character: if the current value is smaller than the next one, I subtract it from my total; otherwise, I add it.

* **Runtime:** 4 ms. Converting the string to a list and scanning it left-to-right takes exactly one pass. Because dictionary lookups take constant time, the solution runs almost instantly at 4 ms.
* **Memory:** 19.4 MB. The only extra storage used is the dictionary for the 7 Roman symbols.