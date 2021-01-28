import pygame as p
from collections import namedtuple

WIDTH = HEIGHT = 600 #512
DIMENSION = 50 # dimensions of a chess board are 8x8
SIZE = HEIGHT // DIMENSION

Position = namedtuple('Position', ['x', 'y'])
top, left, space, lines = (20, 20, 36, 14)
print(lines)
points = [[] for i in range(lines)]
for i in range(lines):
    for j in range(lines):
        points[i].append(Position(left + i * space, top + j * space))
print(points)

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



if __name__ == '__main__':
    p.init()  # pygame initialization
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    p.display.set_caption('SimuTool')

    default_font = p.font.get_default_font()
    font_renderer = p.font.Font(default_font, SIZE)
    running = True

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        draw_board(screen)
        clock.tick(20)
        p.display.flip()

