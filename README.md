# Maze Generator and Solver

This project contains two main components: a maze generator and a maze solver. The maze generator creates a random maze using a recursive algorithm and saves it as an image and a text file, while the maze solver uses depth-first search (DFS) to find a path through the maze and saves the solution as an image.

## Files
maze_generation.py:
  - This script generates a maze using a recursive algorithm and saves it as an image and a text file.

maze_solution.py:
  - This script solves a maze read from a text file using a depth-first search algorithm and saves the solution path as an image.

## Installation
Ensure you have Python installed. You will also need the `Pillow` library for image processing. You can install it using pip:

```
pip install pillow
```

# Maze Generator
## Usage
The maze generator can be run from the command line. It accepts several optional arguments to customize the maze's dimensions and output filenames.

```
python maze_generation.py --width WIDTH --height HEIGHT --image IMAGE_FILENAME --text TEXT_FILENAME
```

## Arguments:
```
--width: Width of the maze (default: 21)
--height: Height of the maze (default: 21)
--image: Filename for the maze image (default: "maze.png")
--text: Filename for the maze text file (default: "maze.txt")
```

## Example

Generate a maze with a width and height of 25, and save the outputs as "my_maze.png" and "my_maze.txt":

```
python maze_generation.py --width 25 --height 25 --image my_maze.png --text my_maze.txt
```

# Maze Solver
## Usage
The maze solver reads a maze from a text file, solves it using DFS, and saves the solution as an image. It can be run from the command line with the following options:


```
python maze_solution.py --maze MAZE_FILENAME --output OUTPUT_FILENAME
```

## Arguments
```
--maze: Filename of the maze text file (default: "maze.txt")
--output: Filename for the solved maze image (default: "maze_solution.png")
```

## Example

Solve a maze from "my_maze.txt" and save the solution as "my_maze_solution.png":

```
python maze_solution.py --maze my_maze.txt --output my_maze_solution.png
```


