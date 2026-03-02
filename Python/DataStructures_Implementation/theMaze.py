class Solution(object):

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        n, m = len(maze), len(maze[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False

        def move_maze(x, y):
            if visited[x][y]:
                return False

            if x == destination[0] and y == destination[1]:
                return True

            visited[x][y] = True

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x, y

                while 0 <= nx + dx < n and 0 <= ny + dy < m and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy

                if move_maze(nx, ny):
                    return True
            return False

        return move_maze(start[0], start[1])
if __name__ == "__main__":
    # Example Maze: 1 is path, 0 is wall
    my_maze = [
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ]
    start = [0, 4]
    destination = [4, 4]
    sol = Solution()

    print(f"Path taken: {sol.hasPath(my_maze,start,destination)}")
