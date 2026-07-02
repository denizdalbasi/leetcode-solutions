# 1967. Number of Strings That Appear as Substrings in a Word

| Language | Approach    | Runtime | Memory   |
| :------- | :---------- | :------ | :------- |
| Python   | Linear Scan | 0 ms    | 19.34 MB |

### Approach Analysis

The problem requires checking how many strings from a given array exist inside a target string (`word`). To solve this efficiently, I iterated through each pattern string in the array and checked for its presence.

Since the lengths of the individual strings and the target word are relatively small, this linear approach quickly checks each string's validity. This allowed me to safely accumulate a total count of valid substrings without wasting unnecessary memory on complex data structures.
