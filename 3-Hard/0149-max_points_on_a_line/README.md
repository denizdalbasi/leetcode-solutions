# 149. Max Points on a Line

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Coprime Slope Hashing | 21 ms | 19.34 MB |

### Approach Analysis
If multiple points have the exact same slope when connected to the same anchor point, they must all be on the same straight line.

My approach looks at every point in the array one by one and uses it as the anchor point. For all other points, it calculates the horizontal change (`dx`) and the vertical change (`dy`). The hardest part is avoiding floating-point number mistakes and handling vertical lines, because dividing by zero or using decimals can cause bugs in programming.

To fix this problem completely without dividing, I used `math.gcd` (Greatest Common Divisor) to simplify the fraction `(dy, dx)` to its smallest possible whole numbers. For example, a change of `(4, 2)` becomes `(2, 1)`. I also made sure that opposite directions have the same sign. These simplified pairs are stored as keys in a dictionary (hash map) to count how many times each slope appears for that specific anchor point. Finally, the highest count plus 1 (for the anchor point itself) gives us the answer.