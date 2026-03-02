def isSafe(maze, x , y , n,  visited):
    # checking dead end wall and index within bound
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

def solve_maze(maze):
    path = []
    n = len(maze)
    visited = [[False for _ in range(n)]for _ in range(n)]

    # explicit check if start and end is a wall
    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return "No Solution Found"

    if move_rat(maze, 0, 0 ,n, path, visited):
        return path
    return "No Solution Found"

def move_rat(maze,x,y,n,path,visited):

    # check if it's a wall
    if not isSafe(maze,x,y,n,visited):
        return False

    visited[x][y] = True
    path.append((x, y))

    # check base condition
    if x == n-1 and y == n-1:
        return True

    if (move_rat(maze,x,y+1,n,path,visited) or move_rat(maze, x+1, y, n, path, visited) or
        move_rat(maze, x, y-1, n, path, visited) or
        move_rat(maze, x-1, y, n, path, visited)):
        return True

    visited[x][y] = False
    path.pop()
    return False

if __name__ == "__main__":
    # Example Maze: 1 is path, 0 is wall
    my_maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    print(f"Path taken: {solve_maze(my_maze)}")
