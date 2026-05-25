# 50. Pow(x, n)

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Binary Exponentiation | 0 ms | 19.54 MB |

### Approach Analysis
To avoid a slow linear loop, first, it handles negative exponents by converting $x^n$ into $(1/x)^{-n}$. 

Inside the loop, the algorithm squares the `current_product` and halves the exponent (`n //= 2`) at each step. Whenever `n` is odd (`n % 2 == 1`), the extra multiplied factor is absorbed into the `result`. This drastically cuts down the total number of multiplication steps needed.
