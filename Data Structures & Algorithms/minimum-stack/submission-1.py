class MinStack:

    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min:
            self.min.append(val)
        else:
            if val < self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])

    def pop(self) -> None:
        self.items.pop()
        self.min.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]
