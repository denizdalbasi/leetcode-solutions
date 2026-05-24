# 4. Median of Two Sorted Arrays

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Built-in Timsort Optimization (Fast) | 4 ms | 19.5 MB |
| Python | Manual Selection Sort (Slow) | 694 ms | 19.4 MB |

### Approach Analysis
I implemented two different ways to solve this problem to compare how algorithm choice impacts real-world performance. Both approaches merge the arrays, find the middle index, and calculate the median depending on whether the total length is odd or even.

* **Slow Solution - 694 ms:** In my first attempt, I combined the lists and used a manual nested-loop selection sort algorithm with `.pop()` and `.insert()`. This created a huge overhead, which made the execution slow.
* **The Optimization (Fast Solution - 4 ms):** To fix this, I swapped out the manual sorting loops for Python's native `sorted()` function (which runs on Timsort). This brought the sorting time down.