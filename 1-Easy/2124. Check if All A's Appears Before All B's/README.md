# 2124. Check if All A's Appears Before All B's

| Language | Approach             | Runtime | Memory   |
| :------- | :------------------- | :------ | :------- |
| Python   | Unique Set Filtering | 0 ms    | 18.98 MB |

### Approach Analysis

The function scans `s` from left to right using a boolean flag `seen_b` (initially `False`) to remember if a `'b'` has appeared yet. Whenever it encounters a `'b'`, it sets `seen_b` to `True`. Whenever it encounters an `'a'`, it checks `seen_b` and immediately returns `False` if a `'b'` was already seen earlier. If the loop reaches the end of the string without finding an `'a'` after a `'b'`, it returns `True`.
