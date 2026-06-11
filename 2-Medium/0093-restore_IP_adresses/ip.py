class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        
        # If the string is too short or too long, it's impossible to form a valid IP
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start: int, current_path: list[str]):
            # Base Case: If we have 4 segments and used the entire string
            if len(current_path) == 4:
                if start == len(s):
                    res.append(".".join(current_path))
                return
            
            # Try segments of length 1, 2, and 3
            for length in range(1, 4):
                # Ensure we don't go out of bounds
                if start + length > len(s):
                    break
                    
                segment = s[start : start + length]
                
                # Check for leading zero: length > 1 and starts with '0'
                if len(segment) > 1 and segment[0] == '0':
                    continue
                    
                # Check value constraint
                if int(segment) > 255:
                    continue
                    
                # Take step: add segment to path and recurse
                current_path.append(segment)
                backtrack(start + length, current_path)
                # Clean up / Backtrack
                current_path.pop()

        backtrack(0, [])
        return res