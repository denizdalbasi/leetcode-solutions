# 2069. Walking Robot Simulation II

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Flat Perimeter Mapping (Modulo Arithmetic) | 34 ms | 24.39 MB |

### Approach Analysis
The robot only moves along the outer boundary of the grid. Instead of simulating step-by-step or handling complex coordinate checks, I flattened the entire perimeter into a 1D array of `(position, direction)` pairs.

The only tricky part is a specific edge case at `(0, 0)`. The robot starts out facing **East**. However, if it travels a full lap (or multiple laps) and lands back at `(0, 0)`, it will be facing **South**, as it arrives from the top of the leftmost column. I used a boolean flag (`moved`) to track this change.