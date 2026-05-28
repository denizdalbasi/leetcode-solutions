class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.mod = 2 * (width + height - 4) + 4
        self.curr_steps = 0
        self.moved = False  

        self.perimeter = []
        
        for x in range(width):
            self.perimeter.append(((x, 0), "East"))

        for y in range(1, height):
            self.perimeter.append(((width - 1, y), "North"))

        for x in range(width - 2, -1, -1):
            self.perimeter.append(((x, height - 1), "West"))

        for y in range(height - 2, 0, -1):
            self.perimeter.append(((0, y), "South"))

    def step(self, num: int) -> None:
        self.moved = True
        self.curr_steps = (self.curr_steps + num) % self.mod

    def getPos(self) -> list[int]:
        pos, _ = self.perimeter[self.curr_steps]
        return list(pos)

    def getDir(self) -> str:
        if self.moved and self.curr_steps == 0:
            return "South"
        
        _, direction = self.perimeter[self.curr_steps]
        return direction