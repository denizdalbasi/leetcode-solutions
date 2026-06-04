# 3751. Total Waviness of Numbers in Range I

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Relative Counting | 412 ms | 16.48 MB |

### Approach Analysis
This solution checks the "waviness" of numbers between `num1` and `num2`. To save memory and time, it does not change numbers into text strings. Instead, it uses math to find the digits.

* **`Finding Digits`**: The code breaks down each number using math rules (like using modulo 10 and division). This helps to separate the number into a list of single digits quickly.
* **`Checking Peaks and Valleys`**: The code looks at the digits from the second digit to the second-to-last digit. It looks for a "Peak" (a digit that is bigger than the digits next to it) or a "Valley" (a digit that is smaller than the digits next to it).
* **`Adding up the Total`**: The code counts these peaks and valleys for every number in the range and adds them together to get the final total score.
