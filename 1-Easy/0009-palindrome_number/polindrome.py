class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        num_list = [int(digit) for digit in str(x)]
        left = 0
        right = len(num_list) - 1
        
        while left < right:
            if num_list[right] == num_list[left]:
                left += 1   
                right -= 1  
            else:
                return False
                
        return True