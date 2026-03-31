class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()
        self.count = 1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.q.remove(key)
        if key not in self.cache and len(self.cache) == self.capacity:
            min_key = self.q.popleft()
            del self.cache[min_key]
    
        self.q.append(key)    
        self.cache[key] = value


