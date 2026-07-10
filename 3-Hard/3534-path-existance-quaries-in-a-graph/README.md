# 3534. Path Existence Queries in a Graph II

| Language | Approach                | Runtime | Memory   |
| :------- | :---------------------- | :------ | :------- |
| Python   | Greedy + Binary Lifting | 2039 ms | 83.44 MB |

### Approach Analysis

The problem asks us to find the shortest path (minimum steps) between two nodes in a graph. An edge exists between two nodes if the absolute difference between their numbers is at most `maxDiff`. Since the constraints are very large, standard graph search algorithms like BFS will be too slow.

I solved this by converting the graph into a one-dimensional "jump game" and using a technique called Binary Lifting.

1. **Sort the Numbers**: I paired each number with its original index and sorted them by value. This allows us to think about the problem as moving from smaller values to larger values.
2. **Greedy Next Steps**: To move from a smaller value to a larger value in the fewest steps, we should always make the largest jump possible. Using two pointers, I found the farthest node each element can reach within `maxDiff`.
3. **Build the Jump Table (Binary Lifting)**: Instead of jumping one by one, I built a table `f[i][k]` that stores where a node ends up after making $2^k$ greedy steps. This allows us to skip many steps at once.
4. **Answer Queries**: For each query, I checked how many greedy leaps are needed to reach or pass the target value. If even our maximum leaps cannot reach the target, a path does not exist and we return `-1`. Otherwise, we return the total number of steps.
