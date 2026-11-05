# 1385. Find the Distance Value Between Two Arrays

| Language | Approach  | Runtime | Memory   |
| :------- | :-------- | :------ | :------- |
| Python   | For loops | 81 ms   | 19.27 MB |

### Approach Analysis

The find the distance all each elements I ran two for loops where once of them calulates distance for arr1 and the other one runs for a spesific arr1 value distance between each elements of arr2. After calualting distance if at least 1 value is less then zero I set up all elements to zero to not count go up by 1. But if all the distancces calculated I check if the minimum element is bigger than d, if yes it means all elements are higher than d, as a result increase the count value by 1 and finally return the count for the final result.
