# 1622. Fancy Sequence

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Lazy Propagation via Modular Inverse | 327 ms | 56.12 MB |

### Approach Analysis
Modifying every element in the array during `addAll` or `multAll`. Instead, I keept track of global operations using a linear equation state: `(value * mult) + add`.

* **`addAll` and `multAll`** execute by just updating the global `add` and `mult` variables.
* **`append`** I stored a "neutralized" version of the number so that when the current global operations are applied to it later, it scales up to exactly its original value.
* **`getIndex`** scales the stored baseline value using the current global state.