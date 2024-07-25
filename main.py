import pygame as pg, time, random, sys
from pygame.locals import *

pg.init()

width = 600
height = 800
winner_line =  (117, 11, 240)#(178, 34, 34)
gray = (43, 45, 48)#(29, 29, 27)
dark_gray = (30, 31, 34)
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Tic Tac Toe")

move = None
winner = None
game_draw = False

background_img = pg.image.load('background.jpg')
screen.blit(background_img, (0, 0))

x_img = pg.image.load('X.png')
x_img = pg.transform.scale(x_img, (100, 100))
o_img = pg.image.load('O.png')
o_img = pg.transform.scale(o_img, (100, 100))
board_img = pg.image.load('board.png')
board_img = pg.transform.scale(board_img, (550, 550))
board_img.set_alpha(200)
board_rect = board_img.get_rect(center = (width // 2, height // 2))

r1 = pg.Rect((10, 110, 580, 580))
radius=10
pg.draw.rect(screen, gray, r1, border_radius=radius)
screen.blit(board_img, board_rect)

r2 = pg.Rect((100, 30, 400, 60))
radius=10
pg.draw.rect(screen, gray, r2, border_radius=radius)

font = pg.font.Font(None, 36)
text1 = None

XO = 1 #-1 is X, 1 is O
text1 = font.render('Ходит Нолик', 1, (225, 227, 231))
place1 = text1.get_rect(center=(300, 60))
screen.blit(text1, place1)

again_rect = pg.Rect((200, 200, 200, 200))
radius=10

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
program_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# 0,1,2 - upper row
# 3,4,5 - middle row
# 6,7,8 - lower row

pg.display.update()

def again_game(screen):
    global text1, place1
    clear_rect = pg.Rect(0, 0, 600, 800)  # Примерная область
    # Очистим область
    screen.fill(dark_gray, clear_rect)
    text1 = font.render('Сыграть еще раз?', 1, (225, 227, 231))
    place1 = text1.get_rect(center=(300, 60))
    screen.blit(text1, place1)
    pg.display.update()

def quit_game():
    game_status()
    pg.display.update()
    time.sleep(4)
    again_game(screen)

def game_status():
    global text1, game_draw
    if winner is None and XO == -1:
        print("X's turn")
        pg.draw.rect(screen, gray, r2, border_radius=radius)
        text1 = font.render('Ходит Крестик', 1, (225, 227, 231))
        place1 = text1.get_rect(center=(300, 60))
        screen.blit(text1, place1)
    if winner == -1:
        print("X won!")
        pg.draw.rect(screen, gray, r2, border_radius=radius)
        text1 = font.render('Крестик выиграл!', 1, (225, 227, 231))
        place1 = text1.get_rect(center=(300, 60))
        screen.blit(text1, place1)

    if winner is None and XO == 1:
        print("O's turn")
        pg.draw.rect(screen, gray, r2, border_radius=radius)
        text1 = font.render('Ходит Нолик', 1, (225, 227, 231))
        place1 = text1.get_rect(center=(300, 60))
        screen.blit(text1, place1)
    if winner == 1:
        print("O won!")
        pg.draw.rect(screen, gray, r2, border_radius=radius)
        text1 = font.render('Нолик выиграл!', 1, (225, 227, 231))
        place1 = text1.get_rect(center=(300, 60))
        screen.blit(text1, place1)

    if game_draw == True:
        print("Draw!")
        pg.draw.rect(screen, gray, r2, border_radius=radius)
        text1 = font.render('Ничья!', 1, (225, 227, 231))
        place1 = text1.get_rect(center=(300, 60))
        screen.blit(text1, place1)
    pg.display.update()

def drawXO():
    global board, XO, move, program_board, x_img_alpha
    if move == None:
        print("The cell is not empty")
    else:
        board[move] = XO
        if move == 0:
            posx = 90
            posy = 190
            program_board.pop(0)
            program_board.insert(0, 1)
        if move == 1:
            posx = 250
            posy = 190
            program_board.pop(1)
            program_board.insert(1, 1)
        if move == 2:
            posx = 410
            posy = 190
            program_board.pop(2)
            program_board.insert(2, 1)

        if move == 3:
            posx = 90
            posy = 350
            program_board.pop(3)
            program_board.insert(3, 1)
        if move == 4:
            posx = 250
            posy = 350
            program_board.pop(4)
            program_board.insert(4, 1)
        if move == 5:
            posx = 410
            posy = 350
            program_board.pop(5)
            program_board.insert(5, 1)

        if move == 6:
            posx = 90
            posy = 510
            program_board.pop(6)
            program_board.insert(6, 1)
        if move == 7:
            posx = 250
            posy = 510
            program_board.pop(7)
            program_board.insert(7, 1)
        if move == 8:
            posx = 410
            posy = 510
            program_board.pop(8)
            program_board.insert(8, 1)
        if XO == -1:
            screen.blit(x_img, (posx, posy))
        else:
            screen.blit(o_img, (posx, posy))
        check_win()

        if game_draw != True:
            XO = -1 * XO
        pg.display.update()

def user_click(): # mouse click
    global move, program_board
    move = None
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get x,y of mouse click (cell 1-9)
    if (y < height / 3) and (x < width / 3):
        if program_board[0] != 1:
            move = 0
    elif (y < height / 3) and (x < width / 3 * 2):
        if program_board[1] != 1:
            move = 1
    elif (y < height / 3) and (x < width):
        if program_board[2] != 1:
            move = 2

    elif (y < height / 3 * 2) and (x < width / 3):
        if program_board[3] != 1:
            move = 3
    elif (y < height / 3 * 2) and (x < width / 3 * 2):
        if program_board[4] != 1:
            move = 4
    elif (y < height / 3 * 2) and (x < width):
        if program_board[5] != 1:
            move = 5

    elif (y < height) and (x < width / 3):
        if program_board[6] != 1:
            move = 6
    elif (y < height) and (x < width / 3 * 2):
        if program_board[7] != 1:
            move = 7
    elif (y < height) and (x < width):
        if program_board[8] != 1:
            move = 8
    drawXO()
    game_status()
    print(board)
    print(program_board)
    pg.display.update()

def check_win():
    global winner, game_draw

    #X for vert
    if board[0] == board[3] == board[6] == -1:
        pg.draw.line(screen, winner_line, [140, 150], [140, 650], 5)
        winner = -1
        quit_game()
    if board[1] == board[4] == board[7] == -1:
        pg.draw.line(screen, winner_line, [300, 150], [300, 650], 5)
        winner = -1
        quit_game()
    if board[2] == board[5] == board[8] == -1:
        pg.draw.line(screen, winner_line, [460, 150], [460, 650], 5)
        winner = -1
        quit_game()
    #X for horis
    if board[0] == board[1] == board[2] == -1:
        pg.draw.line(screen, winner_line, [50, 240], [550, 240], 5)
        winner = -1
        quit_game()
    if board[3] == board[4] == board[5] == -1:
        pg.draw.line(screen, winner_line, [50, 400], [550, 400], 5)
        winner = -1
        quit_game()
    if board[6] == board[7] == board[8] == -1:
        pg.draw.line(screen, winner_line, [50, 560], [550, 560], 5)
        winner = -1
        quit_game()
    #X for diag \
    if board[0] == board[4] == board[8] == -1:
        pg.draw.line(screen, winner_line, [50, 150], [550, 650], 5)
        winner = -1
        quit_game()
    #X for diag /
    if board[2] == board[4] == board[6] == -1:
        pg.draw.line(screen, winner_line, [550, 150], [50, 650], 5)
        winner = -1
        quit_game()

    #O for vert
    if board[0] == board[3] == board[6] == 1:
        pg.draw.line(screen, winner_line, [140, 150], [140, 650], 5)
        winner = 1
        quit_game()
    if board[1] == board[4] == board[7] == 1:
        pg.draw.line(screen, winner_line, [300, 150], [300, 650], 5)
        winner = 1
        quit_game()
    if board[2] == board[5] == board[8] == 1:
        pg.draw.line(screen, winner_line, [460, 150], [460, 650], 5)
        winner = 1
        quit_game()
    #O for horis
    if board[0] == board[1] == board[2] == 1:
        pg.draw.line(screen, winner_line, [50, 240], [550, 240], 5)
        winner = 1
        quit_game()
    if board[3] == board[4] == board[5] == 1:
        pg.draw.line(screen, winner_line, [50, 400], [550, 400], 5)
        winner = 1
        quit_game()
    if board[6] == board[7] == board[8] == 1:
        pg.draw.line(screen, winner_line, [50, 560], [550, 560], 5)
        winner = 1
        quit_game()
    #O for diag \
    if board[0] == board[4] == board[8] == 1:
        pg.draw.line(screen, winner_line, [50, 150], [550, 650], 5)
        winner = 1
        quit_game()
    #O for diag /
    if board[2] == board[4] == board[6] == 1:
        pg.draw.line(screen, winner_line, [550, 150], [50, 650], 5)
        winner = 1
        quit_game()

    if program_board.count(0) == 0 and winner is None:
        game_draw = True
        quit_game()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            user_click()