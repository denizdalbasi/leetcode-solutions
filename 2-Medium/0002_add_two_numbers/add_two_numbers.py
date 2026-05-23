# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = 0
        second_number = 0
        
        first_list_multiplier = 1
        second_list_multiplier = 1
        
        current_l1 = l1
        current_l2 = l2
        
        while current_l1:
            first_number += current_l1.val * first_list_multiplier
            first_list_multiplier *= 10
            current_l1 = current_l1.next  
            
        while current_l2:
            second_number += current_l2.val * second_list_multiplier
            second_list_multiplier *= 10
            current_l2 = current_l2.next 
        total_sum = first_number + second_number
        
        reversed_sum_digits = list(map(int, str(total_sum)[::-1]))
        
        dummy_head = ListNode(0)
        current_output_node = dummy_head
        
        for digit in reversed_sum_digits:
            current_output_node.next = ListNode(digit)
            current_output_node = current_output_node.next
            
        return dummy_head.next