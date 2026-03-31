class MyHashSet:

    def __init__(self):
        self.hashset = [None] * 1000000

    def add(self, key: int) -> None:
        self.hashset[key] = key
        

    def remove(self, key: int) -> None:
        self.hashset[key] = None        

    def contains(self, key: int) -> bool:
        return self.hashset[key] != None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)