class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start: int, current_path: list[str]):
            if len(current_path) == 4:
                if start == len(s):
                    res.append(".".join(current_path))
                return
            
            for length in range(1, 4):
                if start + length > len(s):
                    break
                    
                segment = s[start : start + length]
                
                if len(segment) > 1 and segment[0] == '0':
                    continue
                    
                if int(segment) > 255:
                    continue
                    
                current_path.append(segment)
                backtrack(start + length, current_path)
                current_path.pop()

        backtrack(0, [])
        return res