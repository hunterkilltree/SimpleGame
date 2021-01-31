import pygame as p
from collections import namedtuple
from Robot import *

WIDTH = HEIGHT = 600  # 512
DIMENSION = 50  # dimensions of a chess board are 8x8
SIZE = HEIGHT // DIMENSION
n = 6
Position = namedtuple('Position', ['x', 'y'])
top, left, space, lines = (20, 20, 100, n)  # space 100 / 2 keep the car in the line
print(lines)
points = [[] for i in range(lines)]
for i in range(lines):
    for j in range(lines):
        points[i].append(Position(left + i * space, top + j * space))

# map coordinate with specific point using dict
my_dict = {}  # store Node reference to the position in grip map
for r in range(n):
    for c in range(n):
        coordinate = str(r) + str(c)
        temp = {coordinate: points[r][c]}
        my_dict.update(temp)
print(my_dict)

## map format
'''
Adjacency Matrix 2d array
[
    N1 N2   N3  N4  N5
N1 [ 0   0   0   0   0  ]
N2 [ 0   0   0   0   0  ]
N3 [ 0   0   0   0   0  ]
N4 [ 0   0   0   0   0  ]
N5 [ 0   0   0   0   0  ]
]
Note: > 0 connected points
'''


# TODO: setup Adjacency Matrix function

# TODO: setup Adjacency Matrix function


# TODO: write dijkstra algorithm that return 1D array path


# TODO: write dijkstra algorithm that return 1D array path

# TODO: function move the robot on the line with specific path
speed = 1 # speed must be 1 or 2
def move_robot(x, y, path):
    print(path)
    if path:
        if (x + 10) == my_dict[path[0]].x and (y + 10) == my_dict[path[0]].y:
            print("here")
            path.pop(0)
            return x, y, path
        if (x + 10) < my_dict[path[0]].x:
            x = x + speed
        if (x + 10) > my_dict[path[0]].x:
            x = x - speed

        if (y + 10) < my_dict[path[0]].y:
            y = y + speed
        if (y + 10) > my_dict[path[0]].y:
            y = y - speed

            # x = my_dict[path[0]].x - 10
            # y = my_dict[path[0]].y - 10
    print(x)
    print(y)
    return x, y, path
# TODO: function move the robot on the line


# TODO: constraint valid move

# TODO: constraint valid move


### TEST
# Assume that the shortest path for 3x3 matrix is 10-11-21-22
# shortest_path = ["10", "11", "21", "22"]
shortest_path = ["10", "11", "12", "02"]
shortest_path_back = ["02", "12", "11", "10"]



def color_shortest_path(screen, path):
    color = p.Color("red")
    for i in range(0, len(path) - 1):
        p.draw.line(screen, color, my_dict[path[i]], my_dict[path[i + 1]], 3)


### TEST

# convert to Adjacency Matrix
matrix = []
for point in points:
    print(point)
    temp = []
    for co in point:
        temp.append(2)
    matrix.append(temp)

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=" ")
    print()


# Edge List

# draw grid map
def draw_board(screen):
    # p.draw.line(screen, p.Color("gray"), (-1, -1), (512, 0), 5)
    color = (0, 0, 0)  # Checkerboard grid line color
    color_circle = p.Color("red")

    # Draw coordinate numbers
    for i in range(1, lines):
        coord_text = font_renderer.render(
            str(i),  # The font to render
            True,  # With anti aliasing
            (0, 0, 0))  # RGB Color

        screen.blit(
            coord_text,
            (points[i][0].x - round(coord_text.get_width() / 2), points[i][0].y - coord_text.get_height()))
        screen.blit(
            coord_text,
            (points[0][i].x - coord_text.get_width(), points[0][i].y - round(coord_text.get_height() / 2)))

    for x in range(lines):
        # Draw horizontal lines
        p.draw.line(screen, color, points[0][x], points[lines - 1][x])
        p.draw.circle(screen, color_circle, points[x][0], 2, 0)

        # Draw vertical lines
        p.draw.line(screen, color, points[x][0], points[x][lines - 1])

        p.draw.circle(screen, color_circle, points[0][x], 2, 0)

    # p.draw.line(screen, p.Color("red"), points[0][0], points[0][1], 3)
    # p.draw.line(screen, p.Color("red"), points[0][1], points[1][1], 3)


if __name__ == '__main__':
    p.init()  # pygame initialization
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    p.display.set_caption('SimuTool')

    default_font = p.font.get_default_font()
    font_renderer = p.font.Font(default_font, SIZE)
    running = True

    draw_board(screen)

    picture = p.image.load("images/Robot2.png")
    image = p.transform.scale(picture, (SIZE + 10, SIZE + 10))  # scale the given image fit the grid
    image = p.transform.rotate(image, 90)

    init_pos_x = 70
    init_pos_y = 20
    x = init_pos_x - 10
    y = init_pos_y - 10

    pos = screen.blit(image, p.Rect(x , y , SIZE, SIZE))  # load image into screen

    flag_path = False
    temp_path = []

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False



        key = p.key.get_pressed()
        if key[p.K_0]:
            flag_path = True
            temp_path = shortest_path
            color_shortest_path(screen, shortest_path)
        if key[p.K_9]:
            flag_path = True
            temp_path = shortest_path_back
            color_shortest_path(screen, shortest_path_back)

        if key[p.K_r]:  # reset
            screen.fill(p.Color("white"))  # not good but it work :v

        if flag_path:
            color_shortest_path(screen, temp_path)
            x, y, temp_path = move_robot(x, y, temp_path)
            if not temp_path:
                flag_path = False

        # pos.left = pos.left + 100
        screen.blit(image, p.Rect(x, y, SIZE, SIZE))
        draw_board(screen)
        clock.tick(20)

        # if x == 520:
        #     y = y + 1
        # else:
        #     x = x + 1

        p.display.update()
        p.display.flip()
        screen.fill(p.Color("white"))  # not good but it work :v
