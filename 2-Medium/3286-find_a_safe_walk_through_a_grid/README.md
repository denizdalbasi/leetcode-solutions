# 3286. Find a Safe Walk Through a Grid

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Shortest Path Search | 72 ms   | 19.47 MB |

### Approach Analysis

The problem asks if we can navigate from the top-left corner to the bottom-right corner of a grid without our health dropping to 0. Entering an unsafe cell (`1`) costs 1 health point, while safe cells (`0`) cost nothing.

To solve this efficiently, we want to find the path that loses the **least amount of health possible**.

We can track this using a `while` loop that runs a Breadth-First Search (BFS). We maintain a grid matrix to store the minimum health lost to reach each cell. Starting from `(0,0)`, we explore neighbors in all four directions. If moving to an adjacent cell yields a lower health loss than previously recorded, we update that cell's minimum loss and add it to our processing queue. Once the loop finishes, we check if the minimum health lost to reach the bottom-right destination leaves us with at least 1 health point.
