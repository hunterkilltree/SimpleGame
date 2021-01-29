import pygame as p
from collections import namedtuple

WIDTH = HEIGHT = 600  # 512
DIMENSION = 50  # dimensions of a chess board are 8x8
SIZE = HEIGHT // DIMENSION
n = 5
Position = namedtuple('Position', ['x', 'y'])
top, left, space, lines = (20, 20, 100, n)
print(lines)
points = [[] for i in range(lines)]
for i in range(lines):
    for j in range(lines):
        points[i].append(Position(left + i * space, top + j * space))

# map coordinate with specific point using dict
# TO DO
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

### TEST
# Assume that the shortest path for 3x3 matrix is 10-11-21-22
shortest_path = ["10", "11", "21", "22"]


# for node in shortest_path:
#     print(my_dict[node])

def color_shortest_path(screen):
    color = p.Color("red")
    for i in range(0, len(shortest_path) - 1):
        p.draw.line(screen, color, my_dict[shortest_path[i]], my_dict[shortest_path[i + 1]], 3)


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
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        key = p.key.get_pressed()
        if key[p.K_0]:
            color_shortest_path(screen)
        if key[p.K_r]:  # reset
            screen.fill(p.Color("white"))  # not good but it work :v

        draw_board(screen)
        clock.tick(20)
        p.display.flip()
