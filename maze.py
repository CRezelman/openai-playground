"""Maze Solver using BFS"""
import random
from collections import deque
import numpy as np

def solve_maze_bfs(maze: list[list[int]]):
    """Solve Maze using BFS"""
    start = (1, 0)
    end = (len(maze) - 2, len(maze[0]) - 1)
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

def highlight_path(maze: list[list[int]], path: tuple[int, int]):
    """Highlights solved maze path"""
    if path is None:
        return maze

    highlighted_maze = [row[:] for row in maze]

    for x, y in path:
        highlighted_maze[x][y] = "*"

    return highlighted_maze


def create_maze(dim: int):
    """Create Maze of given dimension"""
    maze = np.ones((dim*2+1, dim*2+1))

    x, y = (0, 0)
    maze[2*x+1, 2*y+1] = 0

    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1, 2*ny+1] == 1:
                maze[2*nx+1, 2*ny+1] = 0
                maze[2*x+1+dx, 2*y+1+dy] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    maze[1, 0] = 0
    maze[-2, -1] = 0

    return (np.ceil(maze)).astype(int).tolist()

# if __name__ == "__main__":
#     maze = create_maze(35)
#     path = solve_maze_bfs(maze)
#     highlighted_maze = highlight_path(maze, path)

#     for row in highlighted_maze:
#         print(" ".join(map(str, row)))
