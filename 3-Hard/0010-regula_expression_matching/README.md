# 10. Regular Expression Matching

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Recursive DFS with Memoization | 7 ms | 20.9 MB |

### Approach Analysis
The challenge was  `*`, because it can mean matching a character multiple times or completely ignoring it. To handle this, I set up a recursive Depth-First Search (DFS) that treats the problem like a decision tree. Every time I hit a `*`, the code splits into two choices: do we skip completely (0 matches), or do we match the current character and keep active for the next step?

* **Runtime:** 7 ms. I fixed speed by using Python's `@cache` decorator. It memorizes the results of index states `(i, j)` we’ve already visited, speeding the compiler.