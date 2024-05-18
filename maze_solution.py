import argparse
from PIL import Image, ImageDraw


def read_maze_from_file(filename):
    with open(filename, "r") as f:
        maze = [list(map(int, line.strip())) for line in f]

    return maze


def solve_maze_dfs(maze, start, end):
    stack = [(start, [])] # текущая точка, путь до текущей точки
    visited = set() # посещенные 

    while stack:
        current, path = stack.pop() # текущая точка, путь до текущей точки

        if current == end: # если текущая = конечная
            return path + [current] # путь от начально до конечной

        if current in visited: 
            continue

        visited.add(current) # пометка о посещении

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # просмотр соседей текущей точки
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 1 and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [current])) # в стек с обновленным путем

    return None # если нет пути от начальной до конечной точки


def draw_solution(maze, solution, filename):
    if solution is None:
        print("No solution found.")
        return

    img = Image.new("RGB", (len(maze[0]), len(maze)), color="black")
    draw = ImageDraw.Draw(img)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw.point((x, y), fill=(255, 255, 255))
            else:
                draw.point((x, y), fill=(0, 0, 0))

    start, end = solution[0], solution[-1]

    for x, y in solution:
        if (x, y) == start or (x, y) == end:
            draw.point((x, y), fill=(255, 0, 0))
        else:
            draw.point((x, y), fill=(0, 255, 0))

    img.save(filename)


def main():
    parser = argparse.ArgumentParser(description="Решение лабиринта с использованием алгоритма поиска в глубину (DFS).")
    parser.add_argument("--maze", type=str, default="maze.txt", help="Имя файла с лабиринтом")
    parser.add_argument("--output", type=str, default="maze_solution.png", help="Имя файла для изображения с решением")

    args = parser.parse_args()

    maze = read_maze_from_file(args.maze)

    start = (1, 1)
    end = (len(maze[0]) - 2, len(maze) - 2) 

    solution_path = solve_maze_dfs(maze, start, end)

    if solution_path:
        draw_solution(maze, solution_path, args.output)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
