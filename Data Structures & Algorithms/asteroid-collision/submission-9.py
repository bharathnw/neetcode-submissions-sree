class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for stone in asteroids:

            while stack and (stack[-1] > 0 and stone < 0):
                if abs(stack[-1]) == abs(stone):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(stone):
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(stone)
        
        return stack

        