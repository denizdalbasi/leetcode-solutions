class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in char_index_map and char_index_map[current_char] >= left:
                left = char_index_map[current_char] + 1
            char_index_map[current_char] = right
            
            current_window_size = right - left + 1
            if current_window_size > max_length:
                max_length = current_window_size
                
        return max_length