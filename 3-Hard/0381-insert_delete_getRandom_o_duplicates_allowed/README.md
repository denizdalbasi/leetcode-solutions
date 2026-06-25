# 381. Insert Delete GetRandom O(1) - Duplicates allowed

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Array with Hash Map of Index Sets | 123 ms | 67.85 MB |

### Approach Analysis
The goal of this problem is to create a collection where we can add numbers, delete numbers, and pick a random number very quickly (instantly), even if the same number is added multiple times.

To pick a random number instantly, we must keep all our numbers in a simple list. This lets the computer pick a random spot in the list without any extra work. However, there is a problem: if you delete a number from the middle of a normal list, the computer has to slide all the other numbers over to fill the empty space. This sliding makes the program slow.

To fix this and keep things fast, my approach uses a smart trick with a helper list and a tracking notebook (a dictionary). The notebook remembers exactly where each number is sitting in our list.
* **When we add a number**: We put it at the very end of our list and write down its position in our notebook.
* **When we delete a number**: We look up its position in our notebook. Instead of sliding all the other numbers over, we take the very last number from the end of the list and move it into the empty spot. Then, we update our notebook with the new position of that moved number, and erase the old number from the end. Because we only move the last number, the computer never has to slide anything, keeping the program incredibly fast.