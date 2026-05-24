# 3. Longest Substring Without Repeating Characters

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Sliding Window (Hash Map Optimized) | 7 ms | 19.3 MB |

### Approach Analysis
I used the two pointers (`left` and `right`) to track the current substring. Instead of shrinking the window step-by-step when a duplicate character appeared, I used a dictionary (`char_index_map`) to store the last seen index of each character. 

* **Runtime:** 7 ms. Whenever I hit a repeating character that fell inside my current window, I instantly jumped the `left` pointer right past the old character's position. This lookup optimization allowed me to scan the entire string in a single pass without unnecessary inner loops.