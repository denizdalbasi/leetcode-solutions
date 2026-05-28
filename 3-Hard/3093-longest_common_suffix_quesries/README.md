# 3093. Longest Common Suffix Queries

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Suffix-to-Prefix Trie | 1235 ms | 165.1 MB |

### Approach Analysis
Reversing the strings turns a suffix match into a prefix match. Instead of doing heavy checks during queries, I handled the tie-breakers on-the-fly when building the Trie. Each node saves a `best_index` pointing to the shortest (and earliest) word that passes through it. If a new word is shorter, or same length but earlier, I updated that node.If a query matches nothing, it drops out instantly at the root and returns the fallback.