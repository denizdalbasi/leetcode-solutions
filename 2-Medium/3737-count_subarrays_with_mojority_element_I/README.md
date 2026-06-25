# 3737. Count Subarrays With Majority Element I

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Balance Tracking Loops | 16 ms | 19.62 MB |

### Approach Analysis
The goal of this problem is to find all the smaller parts (subarrays) of a list where a specific `target` number wins the majority vote. This means the target must appear strictly more than half of the time in that part.

To solve this easily, we can use a point system:
* Every time we see our `target` number, we give it **+1 point**.
* Every time we see any other number, we take away **-1 point**.

Using this rule, if a section of the list has a total score greater than 0, it means the `target` appeared more than all the other numbers combined. My program uses a loop inside another loop to test every single possible section of the list. It starts at a number, moves forward step-by-step, keeps score, and adds to our total answer whenever the score is above 0. Because the list is small (at most 1000 numbers), this simple method runs very quickly without any complex math.