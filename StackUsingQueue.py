class MyStack:

    def __init__(self):
        self.queue=collections.deque()
      
    def push(self, x: int) -> None:
        queue=self.queue
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue)==0