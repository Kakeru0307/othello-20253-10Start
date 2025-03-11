import pygame

pygame.quit()
#関数

#盤面書くやつ
def draw_grid():
    for i in range(square_num):
        pygame.draw.line(screen, Black, (0, i * square_size), (screen_width, i * square_size), 3)
        pygame.draw.line(screen, Black, (i * square_size, 0), (i * square_size, screen_height), 3)

#円書くやつ
def draw_circle():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, Black, (col_index * square_size + 50, row_index * square_size + 50), 45)
            elif col == -1:
                pygame.draw.circle(screen, White, (col_index * square_size + 50, row_index * square_size + 50), 45)

#おける場所を取得するやつ
def get_validation_positions():
    valid_position_list = []
    for row in range(square_num):
        for col in range(square_num):
            #石が置いていない場所の取得
            if board[row][col] == 0:
                for vx ,vy in vec_table:
                    x = vx + col
                    y = vy + row
                    if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                        while True:
                            x += vx
                            y += vy
                            #マスの範囲内にプレイヤーと異なる石がある場合
                            if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                                continue
                            #プレイヤーと同色の色がある場合
                            elif 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                                valid_position_list.append((col, row))
                                break
                            else:
                                break
    return valid_position_list

def flip_pieces(col, row):
    for vx, vy in vec_table:
        flip_list = []
        x = vx + col
        y = vy + row
        while 0 <= x < square_num and 0 <= square_num and board[y][x] == -player:
            flip_list.append((x, y))
            x += vx
            y += vy
            if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                for flip_x, flip_y in flip_list:
                    board[flip_y][flip_x] = player

#画面の作成
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("オセロ")

#マス
square_num = 8
square_size = screen_width // square_num

#FPS
FPS = 60
clock = pygame.time.Clock()

#色
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 156, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

#ボードの設定(黒が1,白が‐1)
board = [
    [1, -1, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, -1, 1, 0, 0, 0],
#     [0, 0, 0, 1, -1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]
#プレイヤーの設定
player = 1

vec_table = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
    ]

#メインループ
run = True
while run:
    #画面の色
    screen.fill(Green)

    draw_grid()            
    draw_circle()
    vaild_positions_list = get_validation_positions()

    for x, y in vaild_positions_list:
        pygame.draw.circle(screen, Yellow, (x * square_size + 50, y * square_size + 50), 45, 3)
    if len(vaild_positions_list) < 1:
        player *=  -1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = mx // square_size
            y = my // square_size
            if board[y][x] == 0 and (x,y) in vaild_positions_list:
                flip_pieces(x, y)
                board[y][x] = player
                player *= -1
    pygame.display.update()
    clock.tick(FPS)        