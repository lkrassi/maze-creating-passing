import argparse
from PIL import Image
import random


class MazeGenerator:
    def __init__(self):
        self.width = None
        self.height = None
        self.image_filename = None
        self.text_filename = None

    def generate_maze(self):
        maze = [[0] * self.width for _ in range(self.height)]

        def carve(x, y):
            stack = [(x, y)]
            while stack:
                current = stack.pop()
                x, y = current

                maze[y][x] = 1
                directions = [(dx, dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]] # движения во все стороны
                random.shuffle(directions) # рандомно

                for dx, dy in directions:
                    nx, ny = x + 2 * dx, y + 2 * dy # новые координаты на 2 шага
                    if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0: # не за границами, еще не посещена
                        maze[ny][nx] = 1 # проход
                        maze[ny - dy][nx - dx] = 1
                        stack.append((nx, ny))

        carve(1, 1)

        return maze

    def save_maze_image(self, maze):
        img = Image.new("RGB", (self.width, self.height), color="black")
        pixels = img.load()

        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 1:
                    pixels[x, y] = (255, 255, 255)
                else:
                    pixels[x, y] = (0, 0, 0)

        img.save(self.image_filename)

    def save_maze_text(self, maze):
        with open(self.text_filename, "w") as f:
            for row in maze:
                f.write("".join(map(str, row)) + "\n")

    def main(self):
        parser = argparse.ArgumentParser(description="Генерация лабиринта")
        parser.add_argument("--width", type=int, default=21, help="Ширина лабиринта")
        parser.add_argument("--height", type=int, default=21, help="Высота лабиринта")
        parser.add_argument("--image", type=str, default="maze.png", help="Имя файла для изображения")
        parser.add_argument("--text", type=str, default="maze.txt", help="Имя текстового файла")

        args = parser.parse_args()
        self.width = args.width
        self.height = args.height
        self.image_filename = args.image
        self.text_filename = args.text

        maze = self.generate_maze()
        self.save_maze_image(maze)
        self.save_maze_text(maze)


if __name__ == "__main__":
    maze_generator = MazeGenerator()
    maze_generator.main()
