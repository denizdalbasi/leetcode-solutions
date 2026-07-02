# 236. Lowest Common Ancestor of a Binary Tree

| Language | Approach              | Runtime | Memory   |
| :------- | :-------------------- | :------ | :------- |
| Python   | Bottom-Up Tree Search | 111 ms  | 50.74 MB |

### Approach Analysis

The goal is to find the lowest shared "parent" node of two specific target nodes in a family-like tree structure.

To solve this, I searched the tree by looking at the branches from the bottom up. The logic follows a few straightforward rules as it checks each position:

1. If the current spot is empty, or if it is one of the two target nodes I am looking for, I return it immediately.
2. Otherwise, I ask both the left and right branches to look for the targets.

By looking at what the branches return, I can find the answer:

- If both the left and right sides find something, it means the current node is the split point where the two targets separate, making it the lowest common ancestor.
- If only one side returns a result, it means both targets are located down that single pathway, so I pass that result up the tree.
