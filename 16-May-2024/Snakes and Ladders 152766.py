# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

# from collections import deque
# from math import ceil

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Helper to convert board index to coordinates
        def get_coordinates(s):
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col
        
        n2 = n * n
        que = deque([1])
        visited = {1}
        steps = 0
        
        while que:
            for _ in range(len(que)):
                s = que.popleft()
                if s == n2:
                    return steps
                for i in range(1, 7):
                    next_s = s + i
                    if next_s <= n2:
                        r, c = get_coordinates(next_s)
                        if board[r][c] != -1:
                            next_s = board[r][c]
                        if next_s not in visited:
                            visited.add(next_s)
                            que.append(next_s)
            steps += 1
        
        return -1
