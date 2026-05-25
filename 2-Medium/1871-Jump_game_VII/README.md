# 1871. Jump Game VII

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Sliding Window BFS | 111 ms | 23.67 MB |

### Approach Analysis
The trickiest part of this problem is dealing with overlapping jump ranges. If you use a standard BFS or DP, I would have end up scanning the same indices over and over again whenever your jump windows overlap. That hits me with an $O(N \times \text{maxJump})$ time complexity, which guarantees a Time Limit Exceeded (TLE) on larger inputs.

To solve this cleanly in linear time, I paired a standard BFS queue with a boundary tracker I called `far_reached`. 

Instead of mindlessly scanning the entire range from `curr + minJump` to `curr + maxJump` every time, the code dynamically bumps the starting point of the next scan up to `far_reached + 1`. This effectively "remembers" what we've already looked at. Any index that has already been evaluated or pushed to the queue is skipped entirely, flattening the whole traversal into a single, efficient linear scan.
