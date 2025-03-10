import pygame

pygame.quit()
#関数
def draw_grid():
    for i in range(square_num):
        pygame.draw.line(screen, Black, (0, i * square_size), (screen_width, i * square_size), 3)
        pygame.draw.line(screen, Black, (i * square_size, 0), (i * square_size, screen_height), 3)

def draw_circle():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, Black, (col_index * square_size + 50, row_index * square_size + 50), 45)
            elif col == -1:
                pygame.draw.circle(screen, White, (col_index * square_size + 50, row_index * square_size + 50), 45)

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
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
#プレイヤーの設定
player = 1

#メインループ
run = True
while run:
    #画面の色
    screen.fill(Green)

    draw_grid()            
    draw_circle()
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
            if board[y][x] == 0:
                board[y][x] = player
                player *= -1
    pygame.display.update()
    clock.tick(FPS)        