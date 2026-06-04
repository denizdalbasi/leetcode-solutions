# 3317. Find the Number of Possible Ways for an Event

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Combinatorics | 1120 ms | 42.74 MB |

### Approach Analysis
This problem asks us to find how many ways we can group $n$ performers into bands using $x$ different stages, and give each band a score from $1$ to $y$. 

I solved this by counting how many stages actually have performers on them. Let $i$ be the number of active stages (stages with at least one performer), from $1$ up to the maximum possible active stages.

For each possible number of active stages $i$, we multiply three choices together:
1. **Choose the stages**: I picked $i$ stages out of the $x$ total stages. This is calculated using combinations: $\binom{x}{i}$.
2. **Group the performers**: I split the $n$ performers into $i$ groups. We use "Stirling Numbers of the Second Kind" $S(n, i)$ to group them, and then multiply by $i!$ because the stages are different from each other. 
3. **Give scores**: Each of the $i$ playing bands gets a score from $1$ to $y$. There are $y^i$ ways to give these scores.

I calculated these choices for every possible number of active stages $i$, add all the results together, and use modulo $10^9 + 7$ to keep the number from getting too big.
