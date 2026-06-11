class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the initial boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        target = n * n
        
        while num <= target:
            # 1. Traverse from left to right along the top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary down
            
            # 2. Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary left
            
            # 3. Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move the bottom boundary up
            
            # 4. Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Move the left boundary right
            
        return matrix