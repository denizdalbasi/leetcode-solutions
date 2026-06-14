# 3045. Count Prefix and Suffix Pairs II

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Trie with Prefix and Suffix Pairs | 1368 ms (Beats 20.86%) | 247.90 MB (Beats 5.52%) |

### Approach Analysis
I solved this problem by using a special tree structure called a **Trie**. Instead of checking every word against every other word (which takes too much time), we break down each word from both the front and the back at the same time.

* **Storing Pairs:** For each word, we look at the letters as pairs: the first letter with the last letter, the second letter with the second-to-last letter, and so on. We save these pairs in our tree.
* **Counting Matches:** As we add a word into the tree, we check how many times we have seen this exact pattern of pairs before. Every time we follow a path that already exists, it means we found a word that is both a prefix and a suffix of the new word, so we add it to our total score.