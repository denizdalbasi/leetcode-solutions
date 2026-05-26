# 188. Best Time to Buy and Sell Stock IV

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | State-Machine Dynamic Programming | 27 ms | 19.30 MB |

### Approach Analysis
The solution uses a state-machine approach to track the maximum profit for up to $k$ transactions. For each day, two states are maintained for transaction $j$: `buy[j]` (holding a stock) and `sell[j]` (liquidated).

* **`buy[j]`**: $\max(\text{previous buy}, \text{sell}[j-1] - \text{price})$
* **`sell[j]`**: $\max(\text{previous sell}, \text{buy}[j] + \text{price})$

An optimization bypasses the DP if $k \ge n/2$, treating it as an unlimited transaction problem. Tracking only the immediate past states optimizes space complexity from $O(n \times k)$ to $O(k)$.