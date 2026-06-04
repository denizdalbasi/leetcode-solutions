class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waaviness(x: int) -> int:
            s = str(x)
            n = len(s)
            
            if n < 3:
                return 0
            
            waviness_count = 0
            for i in range(1, n - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    waviness_count += 1

                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    waviness_count += 1
                    
            return waviness_count
        return sum(get_waviness(x) for x in range(num1, num2 + 1))