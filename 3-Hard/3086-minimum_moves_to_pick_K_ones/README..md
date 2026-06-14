# 3086. Minimum Moves to Pick K Ones

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Sliding Window and Working with Existing Ones | 185 ms (Beats 8.57%) | 30.03 MB (Beats 44.29%) |

### Approach Analysis
I solved this problem by looking at where the `1`s are already placed. Since we want to collect $k$ items, it is faster to use existing `1`s that are close to each other than to create new ones (unless we really have to).

* **Gathering Existing Items:** I checked groups of existing `1`s using a sliding window. By finding the middle point (median) of these groups, I calculated the shortest number of steps needed to bring them together.
* **Creating Missing Items:** If the existing numbers are not enough to reach $k$, I used the allowed changes to fill the remaining gap. Each change adds a small, fixed cost to the total steps. Combining these two steps gives the lowest possible moves.