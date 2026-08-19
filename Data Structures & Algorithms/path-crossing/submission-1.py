class Solution:
    def isPathCrossing(self, path: str) -> bool:
        'N S'
        'E W'
        maps = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        x, y = 0, 0

        sets = set()

        sets.add((0,0))
        for c in path:
            dx, dy = maps[c]
            x = dx+x
            y = dy+y
            if (x, y) in sets:
                return True
            sets.add((x, y))

        return False