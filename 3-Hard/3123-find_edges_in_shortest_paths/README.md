# 3123. Find Edges in Shortest Paths

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Finding the Shortest Path and Working Backwards | 294 ms | 89.07 MB |

### Approach Analysis
I solved this problem by first finding the shortest way to travel from the start (point 0) to the end. After that, I checked the paths in reverse to find exactly which roads/steps make up the fastest route.

* **Finding the Fastest Route - 294 ms:** I calculated the shortest distance to reach every point starting from the beginning.
* **Working Backwards - Beats 94.78%:** Starting from the end, I move backward step-by-step. If a step matches the math for the shortest distance, I mark it as part of the best path. This makes it easy to see which roads are the most important.