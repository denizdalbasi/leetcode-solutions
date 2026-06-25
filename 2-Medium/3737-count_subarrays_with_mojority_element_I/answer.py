from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_valid_subarrays = 0
        
        # Check every possible starting point
        for i in range(n):
            current_balance = 0
            
            # Expand the subarray to the right
            for j in range(i, n):
                if nums[j] == target:
                    current_balance += 1
                else:
                    current_balance -= 1
                
                # If the balance is greater than 0, target is the majority
                if current_balance > 0:
                    total_valid_subarrays += 1
                    
        return total_valid_subarrays