# 2. Add Two Numbers

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Direct Math Conversion | 0 ms | 19.4 MB |

### Approach Analysis
Instead of dealing with complicated pointer carrying logic, I went through both linked lists and used multipliers ($1, 10, 100 \dots$) to pull out the actual numbers they represented. Once I had the two integers, I just added them together normally.

* **Runtime:** 0 ms. After getting the total sum, I converted it to a string and flipped it using slicing (`[::-1]`). From there, I mapped the digits back into a new linked list. It ignored a lot of conditional checks, which made it run instantly.