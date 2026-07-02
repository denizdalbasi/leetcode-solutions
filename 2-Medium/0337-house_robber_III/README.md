# 337. House Robber III

| Language | Approach                 | Runtime | Memory   |
| :------- | :----------------------- | :------ | :------- |
| Python   | Choice-Based Tree Search | 8 ms    | 20.86 MB |

### Approach Analysis

The problem asks us to steal the maximum amount of money from houses arranged in a tree structure. The only rule is that we cannot rob two houses that are directly connected to each other.

To solve this, I used a bottom-up approach that looks at each house and makes a smart choice based on its branches. For every house, the code returns two numbers:

1. **The maximum money if we DO rob this house:** This means we must skip its direct children, so we add the current house's value to the money made by skipping the next two houses.
2. **The maximum money if we DO NOT rob this house:** This means we are free to either rob or skip its children, so we just take the best possible combination from the left and right sides.

By checking the tree from the bottom houses up to the top, we easily find the best overall plan without repeating any work.
