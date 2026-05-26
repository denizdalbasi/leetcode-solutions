class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        total = 0
        
        for char in unique_chars:
            if char.islower() and char.upper() in unique_chars:
                total += 1
                
        return total