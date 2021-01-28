'''
driver file; handle user input and display current GameState
'''

import pygame as p
import engine

import matplotlib
import networkx
import pandas

WIDTH = HEIGHT = 512
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation
IMAGES = {}

'''
Initialize a global dictionary of images.  This will be called exactly once in the main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bp', 'bR', 'bN', 'bQ', 'bK', 'bB' ]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
main driver for handling user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()  # create constructor of class
    loadImages() # only call once time
    running = True
    sqSelected = () # no square is selected, keep track of the last click of the suer (tuple: (row, col))
    playerClicks = [] # keep track of player clicks  (two tuples: ([(4,5), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN :
                location = p.mouse.get_pos() # (x, y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col): # check user clicked the same square twice then undo
                    sqSelected = () # deselect
                    playerClicks = [] # clear player click
                else :
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2: # after the second click
                    move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # reset user clicks
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
draw the squares on the board
'''

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

            # test
            # color = colors[0]
            # p.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)


'''
draw the pieces on the boards using the current GameState.board
'''
def drawPieces(screen, board):

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
all the graphics with a current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of the squares


if __name__ == '__main__':
    main()
