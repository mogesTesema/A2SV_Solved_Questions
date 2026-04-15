class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque()
        self.length = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.length == self.k:
            return False
        self.deque.append(value)
        self.length += 1

        return True
        

    def insertLast(self, value: int) -> bool:
        if self.length == self.k:
            return False
        self.deque.appendleft(value)
        self.length += 1

        return True

        

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        
        self.deque.pop()
        self.length -= 1
        return True

        

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        
        self.deque.popleft()
        self.length -= 1
        return True
        

    def getFront(self) -> int:
        if self.length > 0:
            return self.deque[-1]
        return -1
        

    def getRear(self) -> int:
        if self.length > 0:
            return self.deque[0]
        return -1
        

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.length == self.k:
            return True
        
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()