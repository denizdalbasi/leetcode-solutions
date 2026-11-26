# 3360. Stone Removal Game

| Language | Approach             | Runtime | Memory |
| :------- | :------------------- | :------ | :----- |
| Python   | Unique Set Filtering | 0 ms    | 19 MB  |

### Approach Analysis

Since Alice starts by removing 10 stones and each subsequent player must remove exactly one fewer stone than the previous opponent. We start with stones = 10 and repeatedly check whether the remaining pile has enough stones for the current move. If it does, we subtract the required stones and decrease the removal amount by 1. We continue until a player cannot make their move. The key is tracking whose turn it is. Since Alice goes first, an odd number of successful moves means Alice wins, while an even number means Bob wins. This allows us to determine the winner without needing to implement separate logic for each player.
