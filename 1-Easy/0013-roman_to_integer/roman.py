class Solution:
    def romanToInt(self, s: str) -> int:
        value_dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        my_list = list(s)
        total = 0
        n = len(my_list)
        
        for i in range(n):
            current_value = value_dic[my_list[i]]
            if i + 1 < n and current_value < value_dic[my_list[i + 1]]:
                total -= current_value
            else:
                total += current_value
                
        return total