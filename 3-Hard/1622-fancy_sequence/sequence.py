class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.vals = []
        
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        
        raw_val = (val - self.add) * pow(self.mult, self.MOD - 2, self.MOD)
        self.vals.append(raw_val % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        
        return (self.vals[idx] * self.mult + self.add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)