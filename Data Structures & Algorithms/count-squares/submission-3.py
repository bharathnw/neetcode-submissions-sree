class CountSquares:

    def __init__(self):
        self.storage = {}
        

    def add(self, point: List[int]) -> None:
        self.storage[(point[0], point[1])] = self.storage.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        print(self.storage)
        for x, y in self.storage.keys():
            if x == px or y == py or abs(x-px) != abs(y-py):
                continue
            res += self.storage.get((x, py), 0) * self.storage.get((px, y), 0) * self.storage.get((x,y), 0)
        return res

        
