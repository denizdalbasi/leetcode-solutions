# 66. Plus One

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Iterative Pointer Rollback | 0 ms | 19.14 MB |

### Approach Analysis
The core logic relies on manually mimicking right-to-left addition using a pointer (`i`) starting at the final index. The trickiest scenario is handling a cascade of carryovers when a number ends in multiple nines (e.g., `[9, 9, 9]`).

My approach immediately adds 1 to the last digit and uses a `while` loop to resolve any values that hit `10`. If a digit reaches 10, it reset it to `0`, decrements the pointer to the left, and increments the neighboring digit. 

To prevent Python's negative indexing from wrapping around and corrupting the array or throwing an `IndexError` on numbers like `999`, I added a guardrail: `if i < 0: break`. If the pointer falls off the left edge of the array, the loop cuts off instantly, and a final check handles prepending a `[1]` to the front to properly scale up the number (e.g., transforming `[0, 0, 0]` into `[1, 0, 0, 0]`).