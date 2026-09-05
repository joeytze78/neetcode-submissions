class MinStack:

    def __init__(self):
        self._items = []
        self._min = []
        
    def top(self) -> int:
        return self._items[-1]

    def push(self, val: int) -> None:
        if len(self._items) > 0:
            if val <= self._min[-1]:
                self._min.append(val)
        else:
            self._min.append(val)
        return self._items.append(val)
        
    def pop(self) -> None:
        val = self._items.pop()
        if self._min[-1] == val:
            self._min.pop()

    def getMin(self) -> int:
        return self._min[-1]
