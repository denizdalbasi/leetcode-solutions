# 93. Restore IP Addresses

| Language | Approach              | Runtime | Memory   |
| :------- | :-------------------- | :------ | :------- |
| Python   | Step-by-Step Guessing | 0 ms    | 19.38 MB |

### Approach Analysis

An IP address is made of four number sections separated by dots (like 192.168.1.1). To find all possible valid combinations from a long string of numbers, I tried placing dots at different positions step-by-step.

To save time, I immediately threw away bad guesses using three simple rules:

1. Each section can only be 1 to 3 numbers long.
2. The number in a section cannot be bigger than 255.
3. A section cannot start with a 0 unless the section is just a single "0".

If a path met all the rules and successfully used up all the numbers, it was saved as a valid IP address.
