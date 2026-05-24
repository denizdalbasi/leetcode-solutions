# 1. Two Sum

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Nested Loops | 1711 ms | 19.8 MB |

### Approach Analysis
This solution uses two nested loops to iterate through the array, checking every possible pair of numbers to see if their sum equals the `target` value.

* **Runtime:** Because I compared each element with every other element in the array, the time scales quadratically. This is slow for large datasets.
